from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio
import random
from datetime import datetime

class SensorAgent(Agent):
    class PerceptionBehaviour(CyclicBehaviour):
        async def run(self):
            disaster_type = random.choice(
                ["Flood", "Fire", "Earthquake", "No Disaster"]
            )
            severity = random.randint(1, 10)

            if disaster_type != "No Disaster":
                log = (
                    f"{datetime.now()} | "
                    f"Disaster: {disaster_type} | "
                    f"Severity Level: {severity}"
                )
                print(log)

            await asyncio.sleep(3)

    async def setup(self):
        print("SensorAgent started. Monitoring environment...")

async def main():
    agent = SensorAgent("sensor@localhost", "samso112233")

    # Manual execution (no XMPP dependency)
    await agent.setup()

    behaviour = agent.PerceptionBehaviour()
    behaviour.agent = agent

    # Run perception loop a few times
    for _ in range(5):
        await behaviour.run()

    print("SensorAgent stopped.")

if __name__ == "__main__":
    asyncio.run(main())
