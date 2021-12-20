# 🖋 _Quill Helper_
>『환생했더니 공작 영애의 악역이 어쩌구...해버렸다?!』 이런 제목은 도대체 어떻게 짓는 거야? 웹소설 작명이 막막한 당신을 도와드려요!

_“웹소설 제목은 왜 조금 다른 느낌일까?”_

함축이 곧 미학인 일반적인 문학 소설 제목과 달리, 웹소설의 제목은 길이가 길거나 설명하는 문장형에 가까운 경우가 많습니다. 내용에 대한 정보 값이 충분히 있어야 하고, 소위 제목으로 '어그로'를 끌어야 작품이 흥한다는 말이 있을 정도죠.

실제로 많은 사람들이 글을 쓰며 어려워하는 것 중 하나가 제목 짓기라는데, 많은 분들이 공감하실 거예요. 레포트를 제출할 때도, 블로그에 일상 포스팅 하나를 올리더라도 제목을 고민하게 되는데... 독자들에게 첫 인상이 되는 소설 제목은 더 신중하게 지어야 할 것입니다. 

어떤 제목을 지어야 내용을 함축할 수 있을지, 이런 식의 작명이 익숙하지 않은 분들도 『_Quill Helper_』 와 함께라면 그 짐을 조금은 덜 수 있을 것입니다.

## 🤗 Hugging Face 🤗
fine-tuning된 모델을 다음과 같이 transfomers 라이브러리에서 곧바로 가져다 사용할 수 있습니다!
```python
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained('honeyd3wy/kobart-titlenaming-v0.3')
tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v2')
```

## FLASK API Deployment
![image](https://user-images.githubusercontent.com/86245237/146728254-b00cf03b-026e-45e8-a152-26166b87286b.png)
![image](https://user-images.githubusercontent.com/86245237/146728897-3d9af2db-de9d-4e80-9b04-f7fa2de32acf.png)
![image](https://user-images.githubusercontent.com/86245237/146728987-3dd1bb99-deec-4d58-b4bf-c6592ce0bdec.png)
![image](https://user-images.githubusercontent.com/86245237/146729046-15c7dd36-bc1e-4e75-ae5f-79ef01272726.png)

### ▫ local
```bash
$ git clone https://github.com/honeyd3wy/quill-helper.git
$ cd quill-helper-app
$ pip install -r requirements.txt
$ FLASK_APP=app flask run
```

### ▫ web
⚠ _[공사중입니다.](https://quill-helper.herokuapp.com/index)_ ⚠  

## 📑 Realease note
### | version 0 |
  - koBART 사전학습 모델을 카카오 페이지의 판타지 소설(판타지+현판+로판) 데이터로 학습
  - `v0.1` : 2 epochs trained
  - `v0.2` : 5 epochs trained
  - `v0.3` : 7 epochs trained

---

# 📋 Modeling & Web Novel Analysis Report
(작성중)

---

## Reference
- [카카오 페이지 - 웹소설](https://page.kakao.com/main?categoryUid=11&subCategoryUid=11000)
- [KoBART](https://github.com/SKT-AI/KoBART)
- [KoBART-summarization](https://github.com/seujung/KoBART-summarization)
- [논문 - BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)
- [[Paper Review] BART (2020) - 우정's Log](https://wooodong.tistory.com/19?category=965248)
