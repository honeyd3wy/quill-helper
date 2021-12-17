import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained('honeyd3wy/kobart-titlenaming-v0.1')
tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v2')

text = """
부모님이 돌아가셨다.
물려받은 재산으로 어찌저찌 빚은 면했지만 딸린 동생만 세 명이다!
가족끼리 찢어져 살 수도 없는 노릇이라 하녀 일을 해 어찌저찌 동생들을 잘 키워냈다.
집안도 다시 일어났겠다 이제 내 인생 찾아서 연애하려는데….

“누님. 그 남자는 버리십시오. 제 주변에 괜찮은 남자를 소개시켜 드리겠습니다.”

첫째 동생 에드워드가 제안했다. 내 동생이지만 피도 눈물도 없는 녀석이 에드워드다.
그런 녀석의 기준에 괜찮은 남자라면 얼마나 쓰레기일지 예상만으로도 무섭다.
그래서 소개팅 제의를 거절하자, 에드워드가 샐쭉하게 웃는다.

“누이. 그 남자 뒷조사를 해 보니까 빚이 오천만 베르크야.”

이어서… 둘째인 다니엘이 놀란 척 말했다.
얘, 다니엘. 그 빚 네가 지게 만들었잖아….

“누나. 누나! 그냥 결혼 같은 거 하지 말고 평생 우리랑 살자!”

그리 말하는 막내, 레오나르드의 옷에 피가 튀어 있었다.
내가 만나던 남자마다 막내를 만나고 나면 이상하게 나를 피하던데…
그리고 네 이름만 들어도 벌벌 떨던데… 아니지…?

난 분명 동생들을 곱게 키우려고 노력했는데… 어쩌다 이렇게 된 걸까?
"""

# 정답 : 흑막 남동생들이 내 연애를 방해한다

input_ids = tokenizer.encode(text)
input_ids = torch.tensor(input_ids)
input_ids = input_ids.unsqueeze(0)
output = model.generate(input_ids, eos_token_id=1, max_length=256, num_beams=5)
output = tokenizer.decode(output[0], skip_special_tokens=True)

print(input_ids)
