def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    prompts = {
         "custom_agent": "You are an concerned about the aggregation or inflamation of public available information could be used by detractors to undermine an individual's reputation. Your primary objective is to analyse text content for potential reputational risks, assessing whether commentators might exaggerate narratives to undermine reputation or invade privacy."
    }

    return prompts.get(agent, "No such agent")



def generate_search_queries_prompt(question):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Compose 15 google search queries to search online that would help "{question}" understand what information about them is publicly available, '\
           f'help them understand their reputation online and understand if there is any adverse media or commentary about them'\
           f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3", "query 4", "query 5", "query 6", "query 7", "query 8", "query 9", "query 10", "query 11", "query 12", "query 13", "query 14", "query 15"]'



def generate_custom_report(question, research_summary):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        research_summary (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """
    return f'"""{research_summary}""" Based on the above information, generate a report for the following' \
           f' individual: "{question}".' \
           ' Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.' \
           ' Include relevant facts, figures, and numbers whenever available.' \
           ' The report should have a minimum length of 2,000 words.'\
           ' Ensure that endnotes should are available with hyperlinks to source material'\
           f' The report should focus on how publicly available information about "{question}" could be used to undermine their reputation'\





def get_report_by_type(report_type):
    report_type_mapping = {
        'custom_report_type': generate_custom_report
    }
    return report_type_mapping[report_type]
