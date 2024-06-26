from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Wordnet.wordnet_functs import match_lemma_list

app = FastAPI()

#how to run uvicorn WordNetEndpoint:app --host 0.0.0.0 --port 8001


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/word_similarity/")
def comparison_endpoint(
        initial: str = '',
        compare: str = '',
        lang1: str = 'spa',
        lang2: str = 'eng',
        limit: int = 5
):
    result_word = []
    result_perc = []
    match = match_lemma_list(initial, compare, lang1,lang2, limit)
    for word in match:
        if word is not None:
            if word['word'] not in result_word and word['word'] != compare and word['word'] != initial:
                result_word.append(word['word'])
                result_perc.append(round(word['percentage'], 2))
    #print(result_word)
    for word in result_word:
        result_perc.append(word)

    print(result_perc)
    if not result_perc:
        result_word = {0.0, initial}
    return result_perc
