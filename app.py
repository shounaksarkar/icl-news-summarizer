import streamlit as st
from langchain_groq import ChatGroq

#First let's create summaries of Three articles which we will use for in-context learning later in our summarization part.

article_1 = """
World's biggest music labels sue over AI copyright
9 hours ago
By Natalie Sherman, 
BBC News
Share
Getty Images  Photo of ABBA, L-R: Bjorn Ulvaeus, Agnetha Faltskog, Anni-Frid Lyngstad, Benny Andersson performing live onstage in Wembley Arena in the UK in 1979Getty Images
The lawsuits say Suno and Udio produce works by artists including ABBA that even devoted fans would struggle to tell was AI-generated
The world's biggest record labels are suing two artificial intelligence (AI) start-ups over alleged copyright violation in a potentially landmark case.
Firms including Sony Music, Universal Music Group and Warner Records say Suno and Udio have committed copyright infringement on an "almost unimaginable scale".
They claim the pair's software steals music to "spit out" similar work and ask for compensation of $150,000 (£118,200) per work.
Suno and Udio did not immediately respond to a request for comment.
The lawsuits, announced on Monday by the Recording Industry Association of America, are part of a wave of lawsuits from authors, news organisations and other groups that are challenging the rights of AI firms to use their work.
Suno, which is based in Massachusetts, released its first product last year and claims more than 10 million people have used its tool to make music.
The company, which has a partnership with Microsoft, charges a monthly fee for its service and recently announced it had raised $125m from investors.
New York-based Udio, known as Uncharted Labs, is backed by high profile venture capital investors such as Andreessen Horowitz.
It released its app to the public in April, achieving near-instant fame for being the tool used to create "BBL Drizzy" - a parody track related to feud between the artists Kendrick Lamar and Drake.
Billie Eilish and Nicki Minaj want stop to 'predatory' AI
Sheryl Crow: 'Resurrecting Tupac with AI is hateful'
In the past, AI firms have argued that their use of the material is legitimate under the fair use doctrine, which allows copyrighted works to be used without a license under certain conditions, such as for satire and news.
Supporters have compared machine learning by AI tools to the way humans learn by reading, hearing and seeing previous works.
But in the complaints, which were filed in federal court in Massachusetts and New York, the record labels say the AI firms are simply making money from having copied the songs.
"The use here is far from transformative, as there is no functional purpose for... [the] AI model to ingest the Copyrighted Recordings other than to spit out new, competing music files," according to the complaints.
The complaints say Suno and Udio produce works like "Prancing Queen" that even devoted ABBA fans would struggle to distinguish from an authentic recording from the band.
Songs cited in the Udio lawsuit include Mariah Carey's "All I Want for Christmas is You" and "My Girl" by The Temptations.
The "motive is brazenly commercial and threatens to displace the genuine human artistry that is at the heart of copyright protection", the record labels said in the lawsuits.
They said there was nothing about AI that excused the firms from "playing by the rules" and warned that the "wholesale theft" of the recordings threatened "the entire music ecosystem".
The lawsuits come just months after roughly 200 artists including Billie Eilish and Nicki Minaj signed a letter calling for the "predatory" use of artificial intelligence (AI) in the music industry to be stopped.
"""
summary_1 = """
**Gist:**
Major music labels sue AI start-ups Suno and Udio for alleged massive copyright infringement, claiming AI-generated music threatens artistic integrity.

**Economic Impact:**
- Lawsuits seek $150,000 (£118,200) per work, potentially impacting Suno and Udio's financial viability and investor confidence.
- Legal fees and settlements could affect future AI music development and industry regulations.

**Social Impact:**
- Debate intensifies over AI's role in music creation, challenging traditional copyright laws and artistic authenticity.
- Artists and industry stakeholders advocate for stricter regulations to protect original creativity and rights.

**All Facts and Figures:**
- Lawsuits filed by Sony Music, Universal Music Group, and Warner Records in federal courts in Massachusetts and New York.
- Suno and Udio accused of producing AI-generated songs like "Prancing Queen" mimicking iconic tracks.
- Suno raised $125 million, collaborates with Microsoft; Udio (Uncharted Labs) gained prominence with "BBL Drizzy" parody.
- AI firms argue fair use; labels allege commercial exploitation and threat to music ecosystem.

**Written by and Source:**
- Written by Natalie Sherman, BBC News
"""


article_2 = """
Wikileaks: Julian Assange freed in US plea deal
4 hours ago
By Bernd Debusmann Jr,
BBC News, Washington
Share
Getty Images Julian Assange in 2017Getty Images
Julian Assange will serve no time in US custody as part of the deal with the justice department
After a years-long legal saga, Wikileaks says that founder Julian Assange has left the UK after reaching a deal with US authorities that will see him plead guilty to criminal charges and go free.
Assange, 52, was charged with conspiracy to obtain and disclose national defence information.
For years, the US has argued that the Wikileaks files - which disclosed information about the Iraq and Afghanistan wars - endangered lives.
Assange spent the last five years in a British prison, from where he was fighting extradition to the US.
According to CBS, the BBC's US partner, Assange will spend no time in US custody and will receive credit for the time spent incarcerated in the UK.
Assange will return to Australia, according to a letter from the justice department.
On X, the platform formerly known as Twitter, Wikileaks said that Assange left Belmarsh prison on Monday after 1,901 days in a small cell.
He was then "released at Stansted airport during the afternoon, where he boarded a plane and departed the UK" to return to Australia, the statement added.
Video shared online by Wikileaks appear to show Assange, dressed in jeans and a blue shirt, being driven to Stansted before boarding an aircraft.
The BBC has been unable to independently verify the video.
His wife, Stella Assange, tweeted thanks to his supporters "who have all mobilised for years and years to make this come true".
The deal - which will see him plead guilty to one charge - is expected to be finalised in a court in the Northern Mariana Islands on Wednesday, 26 June.
The remote Pacific islands, a US commonwealth, are much closer to Australia than US federal courts in Hawaii or the continental US.
Agence France Press quoted a spokesperson for Australia's government as saying that the case had "dragged on for too long".
His attorney, Richard Miller, declined to comment when contacted by CBS. The BBC has also contacted his US-based lawyer.
He and his lawyers had long claimed that the case against him was politically motivated.
In April, US President Joe Biden said that he was considering a request from Australia to drop the prosecution against Assange.
In a victory the following month, the UK High Court ruled that Assange could bring a new appeal against extradition to the US, allowing him to challenge US assurances over how his prospective trial would be conducted and whether his right to free speech would be infringed.
After the ruling, his wife Stella told reporters and supporters that the Biden administration "should distance itself from this shameful prosecution".
US prosecutors had originally wanted to try the Wikileaks founder on 18 counts - mostly under the Espionage Act - over the release of confidential US military records and diplomatic messages related to the wars in Afghanistan and Iraq.
Wikileaks, which Assange founded in 2006, claims to have published over 10 million documents in what the US government later described as "one of the largest compromises of classified information in the history of the United States".
In 2010, the website published a video from a US military helicopter which showed more than a dozen Iraqi civilians, including two Reuters news reporters, being killed in Baghdad.
One of Assange's most well-known collaborators, US Army intelligence analyst Chelsea Manning, was sentenced to 35 years in prison before then-president Barack Obama commuted her sentence in 2017.
Assange also faced separate charges of rape and sexual assault in Sweden, which he denied.
He spent seven years hiding in Ecuador's London embassy, claiming the Swedish case would lead him to be sent to the US.
Swedish authorities dropped the case in 2019 and said that too much time had passed since the original complaint, but UK authorities later took him into custody. He was tried for not surrendering to the courts to be extradited to Sweden.
Even amid long-running legal battles, Assange has rarely been seen in public and for years has reportedly suffered from poor health, including a small stroke in prison in 2021.
"""
summary_2 = """
**Gist:** Julian Assange freed in a US plea deal, allowing him to return to Australia after years of legal battles and imprisonment in the UK.

**Economic Impact:** The case's conclusion may reduce legal and custodial costs for both the US and UK governments.

**Social Impact:** The deal is seen as a significant moment for press freedom advocates and Assange supporters, who have long claimed his prosecution was politically motivated.

**All Facts and Figures:**
- Julian Assange, 52, charged with conspiracy to obtain and disclose national defense information.
- Spent 1,901 days in a British prison.
- Will receive credit for time served in the UK.
- Plea deal to be finalized in Northern Mariana Islands on June 26.
- Wikileaks published over 10 million documents.
- Video of US military killing civilians in Baghdad published in 2010.

**Written by and source:** Bernd Debusmann Jr, BBC News

"""


article_3 = """
Criminal charges recommended against Boeing
6 hours ago
By João da Silva,
Business reporter

Share
Reuters File photo of a Boeing logo on the side of a 737 MAX at the Farnborough International Airshow.Reuters
US prosecutors have recommended that the Department of Justice (DoJ) brings criminal charges against Boeing.
It follows a claim by the DoJ that the plane maker had violated a settlement related to two fatal crashes involving its 737 Max aircraft which killed 346 people.
Boeing declined to comment when contacted by the BBC but previously it has denied violating the deferred prosecution agreement.
The DoJ has until 7 July to make a final decision on whether to prosecute the company. The DoJ has declined to comment.
The recommendation is not a final decision and the details of any potential criminal action are not known, according to CBS, the BBC's US partner.
"This is a really critical decision that is coming up,” said Ed Pierson, who is the executive director of the Foundation for Aviation Safety and a former senior manager at Boeing.
He told the BBC's Radio 4 Today programme: "There are issues with these aeroplanes. We’re seeing problems with these planes and I’m talking about 737 Max, 787 and it is reflective of the leadership."
The plane crashes - both involving Boeing's 737 Max aircraft - occurred within six months of each other.
The crash involving Indonesia's Lion Air occurred in October 2018, following by an Ethiopian Airlines flight in March 2019.
Last week, relatives of the victims urged prosecutors to seek a fine against Boeing of $25bn (£14.6bn) and to pursue a criminal prosecution.
Under a deal reached in 2021, Boeing said it would pay a $2.5bn settlement and prosecutors agreed to ask the court to drop a criminal charge after three years if the company abided by certain stipulations set out in the deferred prosecution agreement.
But last month, the DoJ said Boeing was in breach of the deal, stating that it had failed to "design, implement, and enforce a compliance and ethics program to prevent and detect violations of the US fraud laws throughout its operations".
Boeing crash families demand record $25bn fine
Boeing may face criminal prosecution over 737 Max crashes, US says
Last week, Boeing's outgoing chief executive Dave Calhoun faced a grilling from US senators.

Mr Calhoun testified that the company had "learned" from past mistakes and that the process for employee whistleblowers "works" - but lawmakers still accused him of not doing enough to rectify a culture of retaliation.
As part of an ongoing investigation, Boeing whistleblowers told the Senate in April that the 737 Max, the 787 Dreamliner and the 777 models had serious production issues.
The company was most recently put in the spotlight when a door panel fell off a new 737 Max plane during an Alaska Airlines flight in January, leaving a gaping hole.
Mr Calhoun is stepping down as chief executive at the end of the year
"""
summary_3 = """
**Gist:** US prosecutors recommend criminal charges against Boeing for violating a settlement related to two fatal 737 Max crashes that killed 346 people.

**Economic Impact:** Boeing faces potential fines up to $25 billion, impacting its financial stability and market reputation.

**Social Impact:** Families of crash victims and aviation safety advocates demand accountability, highlighting ongoing concerns about Boeing's safety culture and compliance.

**All Facts and Figures:**
- 346 people killed in two 737 Max crashes (Lion Air in October 2018, Ethiopian Airlines in March 2019).
- Boeing agreed to a $2.5 billion settlement in 2021.
- Potential additional fine of $25 billion requested by victims' families.
- DOJ has until July 7 to decide on prosecution.
- Boeing CEO Dave Calhoun's compensation: $33 million.
- Deferred prosecution agreement involved compliance with US fraud laws.

**Written by and source:** João da Silva, BBC News
"""


examples = [
    {'article': article_1, 'summary': summary_1},
    {'article': article_2, 'summary': summary_2},
    {'article': article_3, 'summary': summary_3}
]

# Initialize LangChain GROQ
llm = ChatGroq(temperature=0.5, groq_api_key="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", model_name="llama3-8b-8192")

# Function to generate default summary
def default_summary(article):
    prompt = f'''
            Summarize the following news article: {article}
            '''
    response = llm.invoke(prompt)
    return response.content

# Function to generate personalized summary
def personalised_summarize(article):
    prompt = f'''
             ### Instructions ###
             You are an expert in summarizing news articles in given format.
             Below are three examples from which you are to learn the format of the summary.
             After that you will be provided with an article, which you have to summarize in the exact format, the format you will learn from the pattern in the examples given below.

             ### Examples 1 ###
             Article: {examples[0]['article']}
             Summary: {examples[0]['summary']}

             ### Example 2 ###
             Article: {examples[1]['article']}
             Summary: {examples[1]['summary']}

             ### Example 3 ###
             Article: {examples[2]['article']}
             Summary: {examples[2]['summary']}

             ### Summarize this article now ###
             Article: {article}
             Summary:
            '''
    response = llm.invoke(prompt)
    return response.content

st.set_page_config(page_title='News Summarizer', page_icon='📚')

# Streamlit app
def main():
    st.title('News Article Summarizer')
    
    st.subheader('Enter the article you want to summarize:')
    user_article = st.text_area('Article:')
    
    if st.button('Generate Summaries'):
        st.markdown('## Default Summary')
        default = default_summary(user_article)
        st.markdown(default)
        
        st.markdown('## Personalized Summary')
        personalised = personalised_summarize(user_article)
        st.markdown(personalised)

if __name__ == '__main__':
    main()
