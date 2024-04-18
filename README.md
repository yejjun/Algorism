symptom = []

flu = ["피로감", "근육통", "관절통", "오한", "전신증상"]  #출처는 인하대병원
cold = ["코막힘", "미열", "콧물", "기침", "인후통", "호흡기 증상"]

cold_symptom = 0
flu_symptom = 0

print("본인의 증상을 입력해주세요 / 1을 입력하면 증상입력이 중단됩니다.")
print("증상 리스트 : 코막힘, 미열, 콧물, 기침, 인후통, 호흡기 증상, 피로감, 근육통, 관절통, 오한, 전신증상")  

while True:
    key = input()
    if key == '1':
        break
    symptom.append(key)

for i in symptom:
    for j in flu:
        if i == j:
            flu_symptom += 1

    for j in cold:
        if i == j:
            cold_symptom += 1

if flu_symptom > 0:
    print("당신의 질병은 독감으로 예상됩니다.")
else:
    print("당신의 질병은 감기로 예상됩니다.")

