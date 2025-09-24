from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def main():
    print("Hello from langchain-start!")
    info = """Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

    Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen."""
    summary_template = """
    given the information {info} about a person I want you to create:
    1. A short summary
    2. 2 interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(temperature = 0, model="gemini-2.5-flash")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"info":info})
    print(response.content)





if __name__ == "__main__":
    main()
