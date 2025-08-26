import os.path

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import PDFSearchTool

PDF_PATH = './knowledge/TheColaTrap.pdf'
OUTPUT_DIR = "output"
SUMMARY_PATH = f"{OUTPUT_DIR}/summary.md"
QUIZ_PATH = f"{OUTPUT_DIR}/quiz.md"
RESULTS_PATH = f"{OUTPUT_DIR}/results.md"



# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BuddyAi():
    """BuddyAi crew"""

    agents: List[BaseAgent]
    tasks: List[Task]



    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def pdf_reader(self) -> Agent:

        return Agent(
            config=self.agents_config['pdf_reader'], # type: ignore[index]
            verbose=True,
            tools=[PDFSearchTool(pdf=PDF_PATH)]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def quiz_maker(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_maker'],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def quiz_buddy(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_buddy'],  # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def reading_task(self) -> Task:
        return Task(
            config=self.tasks_config['reading_task'], # type: ignore[index]
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'], # type: ignore[index]
            output_file=SUMMARY_PATH
        )

    @task
    def create_quiz_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_quiz_task'],  # type: ignore[index]
            output_file=QUIZ_PATH
        )

    @task
    def user_test_task(self) -> Task:

        agent.say("Starting user test task")

        return Task(
            config=self.tasks_config['user_test_task'],  # type: ignore[index]
            output_file=RESULTS_PATH,
        )
    @crew
    def crew(self) -> Crew:
        """Creates the BuddyAi crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
