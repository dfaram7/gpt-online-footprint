# 🔎 GPT Online Footprint

**OSINT Analysts are sometimes required to conduct an assessment of their clients online exposure to determine if there is any risk to their privacy or reputation. The widespread utilisation of LLMs has introduced a new dimension for analysts to explore, as these models fuel automated content generation and contribute to the proliferation of low-quality journalism. GPT Online Footprint employs LLMs to assimilate and interpret open-source information about a target, facilitating the assessment of potential privacy and reputational risks posed by AI.** 

Inspired by [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) and [Research-GPT](https://github.com/assafelovic/gpt-researcher)

## Why GPT Digital Footprint?

- With the rising use of LLMs for content generation among social media users, journalists, and trolls, it becomes important for public figures to understand what data has been used to train these models.
-  Being aware of how LLMs interpret any new information about an individual can help them prepare for future agression and safeguard their interests.
- Awareness of LLM biases can help inform defensive PR/Comms strategies 

## Architecture
The main idea is to run "planner" and "execution" agents, where the planner generates Google queries to best identify problematic articles, and the execution agents process the retrieved information. Finally, the planner filters and aggregates all related information and creates a report. The agents currently leverage gpt3.5-turbo-16k with an option to include gpt-4 in the future.

More specifcally:
* Generate a set of search queries which aim to identify problematic content for the target individual. Some LLM biases will be revealed at this stage 
* For each query, trigger a crawler agent that scrapes online resources for information relevant to the given task.
* For each scraped resources, summarize based on relevant information and keep track of its sources.
* Finally, filter and aggregate all summarized sources and generate a final report.


## Features
- 🌐 Aggregates over 60 web sources per research to form objective and factual conclusions
- 🖥️ Includes an easy-to-use web interface (HTML/CSS/JS)
- 🔍 Scrapes web sources with javascript support
- 📂 Keeps track and context of visited and used web sources
- 📄 Export research reports to PDF and more...

## Quickstart
> **Step 0** - Install Conda and create a Python 3.11 environment: 
```bash
conda create -n py311 python=3.11
```
<br />

> **Step 1** - Activate the environment
```bash
conda activate py311
```

<br />

> **Step 2** - Clone the repo

```bash
$ git clone https://github.com/dfaram7/gpt-online-footprint.git
$ cd gpt-online-footprint
```

<br />

> **Step 3** - Install dependencies
```bash
$ pip install -r requirements.txt
```
<br />

> **Step 4** - Install WeasyPrint
```bash
$ conda install -c conda-forge weasyprint
```
<br />

> **Step 5** - Create .env file with your OpenAI Key or simply export it

```bash
$ export OPENAI_API_KEY={Your API Key here}
```
<br />

> **Step 6** - Run the agent with FastAPI

```bash
$ uvicorn main:app --reload
```
<br />

> **Step 7** - Go to http://localhost:8000 on any browser 

- If you are having issues with weasyprint, please visit their website and follow the installation instructions: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html
- Check out the example_reports folder for some examples of the reports created by the tool!
