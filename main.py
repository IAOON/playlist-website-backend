
from fastapi import FastAPI, HTTPException

import uvicorn
import os
import requests
import json

app = FastAPI()

@app.get("/collections/{collection_name}")
async def get_collection_route(collection_name: str):
    if not collection_name == "AKA":
        raise HTTPException(status_code=404, detail="Collection not found")
    else:
        return {"playlist": [{"id" : "PLKsLXjjbcMVfylCbUB_JYGiKuVX62EJhR", "name": "AKA's collection"}]}

@app.get("/playlist/{playlist_id}")
async def get_playlist_route(playlist_id: str):
    # TODO : API key를 어떻게 처리해야할지 고민하기
	key = "AIzaSyBMDMeJl6repf_FGwvKQ4uOCfeN8HEkWnQ"	
	
	url = "https://www.googleapis.com/youtube/v3/playlistItems"

	data = {"key": key, "part": "snippet", "playlistId": playlist_id}

	res = requests.get(url = url, params = data)

	if res.status_code != 200:
        # TODO : log 기록하기
		raise HTTPException(status_code=500, detail="유튜브 API 서버와의 통신 중 문제가 발생했습니다")

	data = json.loads(res.text)
    
	answer = []
    
	for x in data["items"]:
		s = x["snippet"]
		data = {"title": s["title"],
                "detail": s
            }
		answer.append(data)
	return {"songs": answer}

@app.get("/")
async def root():
    return {"message": "배포 성공!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")