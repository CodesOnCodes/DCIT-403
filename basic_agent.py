from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import asyncio

class BasicAgent(Agent):
    class StartBehaviour(OneShotBehaviour):
        async def run(self):
            print("BasicAgent behaviour executed successfully.")

    async def setup(self):
        print("BasicAgent setup completed.")

async def main():
    agent = BasicAgent("basicagent@localhost", "samson112233")

    # Manually call setup (no XMPP connection)
    await agent.setup()

    # Manually execute behaviour
    behaviour = agent.StartBehaviour()
    behaviour.agent = agent
    await behaviour.run()

    print("Agent execution finished.")

if __name__ == "__main__":
    asyncio.run(main())
