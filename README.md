# π _Quill Helper Project_
>γνμνλλ κ³΅μ μμ μ μμ­μ΄ μ΄μ©κ΅¬...ν΄λ²λ Έλ€?!γ μ΄λ° μ λͺ©μ λλμ²΄ μ΄λ»κ² μ§λ κ±°μΌ? μΉμμ€ μλͺμ΄ λ§λ§ν λΉμ μ λμλλ €μ!

_βμΉμμ€ μ λͺ©μ μ μ‘°κΈ λ€λ₯Έ λλμΌκΉ?β_

ν¨μΆκ³Ό μΆμνκ° κ³§ λ―ΈνμΈ μΌλ°μ μΈ λ¬Έν μμ€ μ λͺ©κ³Ό λ¬λ¦¬, μΉμμ€μ μ λͺ©μ κΈΈμ΄κ° κΈΈκ±°λ **μ§κ΄μ μΌλ‘ μ€λͺ**νλ λ¬Έμ₯νμ κ°κΉμ΄ κ²½μ°κ° λ§μ΅λλ€. **λ΄μ©μ λν μ λ³΄ κ°μ΄ μΆ©λΆ**ν μμ΄μΌ νκ³ , μμ μ λͺ©μΌλ‘ 'μ΄κ·Έλ‘'λ₯Ό λμ΄μΌ μνμ΄ ν₯νλ€λ λ§μ΄ μμ μ λμ£ .

μ€μ λ‘ λ§μ μ¬λλ€μ΄ κΈμ μ°λ©° μ΄λ €μνλ κ² μ€ νλκ° μ λͺ© μ§κΈ°λΌλλ°, λ§μ λΆλ€μ΄ κ³΅κ°νμ€ κ±°μμ. λ ν¬νΈλ₯Ό μ μΆν  λλ, λΈλ‘κ·Έμ μΌμ ν¬μ€ν νλλ₯Ό μ¬λ¦¬λλΌλ μ λͺ©μ κ³ λ―Όνκ² λλλ°... λμλ€μκ² μ²« μΈμμ΄ λλ μμ€ μ λͺ©μ λ μ μ€νκ² μ§μ΄μΌ ν  κ²μλλ€.

μ΄λ€ μ λͺ©μ μ§μ΄μΌ νΈλ λμ λ°λΌκ° μ μλ κ±ΈκΉμ? μ΄λ° μμ μλͺμ΄ μ΅μνμ§ μμ λΆλ€λ γ_Quill Helper_γ μ ν¨κ»λΌλ©΄ κ·Έ μ§μ μ‘°κΈμ λ μ μμ κ²μλλ€.

### νλ‘μ νΈ λͺ©ν
1. μΉμμ€ μ₯λ₯΄ λ³ μ λͺ© νΈλ λ λΆμ
2. ννμ§ μ₯λ₯΄ μΉ μμ€ μλͺκΈ° μ΄νλ¦¬μΌμ΄μ κ΅¬ν
    - KoBART abstract summerization tasks fine-tuning

### π [Analysis & Modeling Report](https://www.notion.so/pypyai/Report-Web-Novel-Data-Analysis-Naming-App-744614ee80e64e44ae10b5f6d284ff51)

---
# Deployment

## 1. π€ Hugging Face π€
fine-tuningλ λͺ¨λΈμ λ€μκ³Ό κ°μ΄ transfomers λΌμ΄λΈλ¬λ¦¬μμ κ³§λ°λ‘ κ°μ Έλ€ μ¬μ©ν  μ μμ΅λλ€!

```python
from transformers import BartForConditionalGeneration

# v0.1
model_v1 = BartForConditionalGeneration.from_pretrained('honeyd3wy/kobart-titlenaming-v0.1')
# v0.2
model_v2 = BartForConditionalGeneration.from_pretrained('honeyd3wy/kobart-titlenaming-v0.2')
# v0.3
model_v3 = BartForConditionalGeneration.from_pretrained('honeyd3wy/kobart-titlenaming-v0.3')
```

κ° λͺ¨λΈμ μμλ [μ¬κΈ°](https://www.notion.so/pypyai/Report-Web-Novel-Data-Analysis-Naming-App-744614ee80e64e44ae10b5f6d284ff51#aa481001d1444f74833921cc1ae8c8ef)λ₯Ό μ°Έκ³ ν΄μ£ΌμΈμ.

## 2. FLASK API
![image](https://user-images.githubusercontent.com/86245237/146728254-b00cf03b-026e-45e8-a152-26166b87286b.png)
![image](https://user-images.githubusercontent.com/86245237/146728897-3d9af2db-de9d-4e80-9b04-f7fa2de32acf.png)
![image](https://user-images.githubusercontent.com/86245237/146728987-3dd1bb99-deec-4d58-b4bf-c6592ce0bdec.png)
![image](https://user-images.githubusercontent.com/86245237/146729046-15c7dd36-bc1e-4e75-ae5f-79ef01272726.png)

### β« local
```bash
$ git clone https://github.com/honeyd3wy/quill-helper.git
$ cd quill-helper-app
$ pip install -r requirements.txt
$ FLASK_APP=app flask run
```

### β« web
β  _[κ³΅μ¬μ€μλλ€.](https://quill-helper.herokuapp.com/index)_ β   

## π Realease note
### | version 0 |
  - koBART μ¬μ νμ΅ λͺ¨λΈμ μΉ΄μΉ΄μ€ νμ΄μ§μ ννμ§ μμ€(ννμ§+νν+λ‘ν) λ°μ΄ν°λ‘ νμ΅
  - `v0.1` : 2 epochs trained
  - `v0.2` : 5 epochs trained
  - `v0.3` : 7 epochs trained

---

## Reference
- [μΉ΄μΉ΄μ€ νμ΄μ§ - μΉμμ€](https://page.kakao.com/main?categoryUid=11&subCategoryUid=11000)
- [KoBART](https://github.com/SKT-AI/KoBART)
- [KoBART-summarization](https://github.com/seujung/KoBART-summarization)
- [λΌλ¬Έ - BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)
- [[Paper Review] BART (2020) - μ°μ 's Log](https://wooodong.tistory.com/19?category=965248)
