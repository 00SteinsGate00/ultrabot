import requests

import discord
import asyncio

import metamodule

# Can tell you if the Fachschaft Inforamtik TU KL is currently closed or opened
class FsInfo(metamodule.Meta):

    def get_command(self):
        return 'fsinfo'

    async def help(self, message):
        helpstr = ''' Checks if the Fachschaft Informatik TU KL is locked or not
                - `!%s`: Checks if it's opened or closed
        ''' % self.get_command()

    async def execute(self, command, message):
        # get the JSON status object
        response = requests.get('https://www.fachschaft.cs.uni-kl.de/opendoor.json')
        if(response.status_code == 200):
            # parse it and create the message accordingly
            locked_status = response.json()['opendoor']
            status_message = 'The Fachschaft is currently **%s**' % ('opened' if locked_status else 'closed')
            await self.client.send_message(message.channel, status_message)
        # service seems to be down
        else:
            await self.client.send_message(message.channel, 'Sorry but I couldn\'t reach the Fachschaft...')
