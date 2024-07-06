# News Summarization

## Introduction
- A news summarization application which summarizes articels from cnn website by retrieving articles using web scraper and fedding those articles to our finetuned transformer models.
- Earlier used topic representation to generate summaries by selecting top k import sentences from the given paragraph.
- Moved to an encoder decoder architecture with embeddings generated using word2vec and got rouge-1 precision 0.256 with an accuracy of 0.86.
- Fine tuned transformer models, t5-base and bart-base, and achieved rouge-1 precision of 0.422 and 0.339 respectively.
- Used beautiful soup 4 to create web scraper for cnn website.
- Created interface using streamlit and used the fine tuned transformer model for generating summaries. 


## Technologies Used
- **Interface** - Python (Streamlit)
- **Web Scraping** - Python (Beautiful Soup 4)
- **Encoder Decoder Model** - Python (Tensorflow and Keras) 
- **Transformer Model** - Python (Transformers)

## Running locally
To run **News Summarization application** locally, follow these steps:
1. Clone the repository:
   
   ```bash
   git clone https://github.com/SiddharthVPillai/News_Summarization.git
   cd News_Summarization
   ```

2. Download the transformer models for [t5-base](https://www.kaggle.com/models/siddharth050/t5-fine-tuned) and [bart-base](https://www.kaggle.com/models/siddharth050/bart-fine-tuned).
  
3. Run the streamlit application:
   
    ```bash
      streamlit run main.py
    ```

4. On your web browser goto `localhost:8501`. You will reach the main page of the application as shown below.

   ![image](https://github.com/SiddharthVPillai/News_Summarization/assets/68557526/28295d68-8c94-46e8-93e4-1d450819b8e4)

   To generate summaries paste the link to cnn website and select the model using which you want to generate summaries.

   ![image](https://github.com/SiddharthVPillai/News_Summarization/assets/68557526/ccf3d7ee-94ee-4e16-a01e-cd32ca0a8d37)
  
   ![image](https://github.com/SiddharthVPillai/News_Summarization/assets/68557526/46c795d4-0523-47e3-a3e0-0ca2fefda332)
   
  
