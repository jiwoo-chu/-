import json

# 수질 기준 (환경부 기준)
WATER_QUALITY_STANDARDS = {
    "pH": (6.5, 8.5),
    "전기전도도": (0, 500),           # μS/cm
    "총질소": (0, 3),                # mg/L
    "총대장균군": (0, 1000),         # CFU/100mL
    "용존산소량": (5, 999),           # mg/L (최소치만 중요)
    "생화학적 산소요구량": (0, 3),     # mg/L (낮을수록 좋음)
    "부유물질량": (0, 25),            # mg/L
    "총인": (0, 0.3),                # mg/L
    "총유기탄소": (0, 5)              # mg/L
}

class WaterQualityAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        print(f"[지점명: {self.data.get('지점명', '지점명 없음')}]")
        results = {}  # 결과를 담을 딕셔너리
        issue_count = 0 #기준 벗어난 항목의 개수

        # 각 항목에 대해 수질 기준을 비교
        for 항목, 값 in self.data.items():
            if 항목 == "지점명":
                continue  # 지점명은 기준을 비교하지 않음

            if 항목 in WATER_QUALITY_STANDARDS:
                최소값, 최대값 = WATER_QUALITY_STANDARDS[항목]
                if 최소값 <= 값 <= 최대값:
                    results[항목] = f"적정 ({값})"
                else:
                    results[항목] = f"기준 초과 또는 미달 ({값})"
                    issue_count += 1
            else:
                results[항목] = f"기준 없음 ({값})"
        
        return results , issue_count

    def report(self, results, issue_count):
        print("\n수질 분석 결과:")
        for 항목, result in results.items():
            print(f"- {항목}: {result}")

        print("\n종합 판단:") #\n은 문단 띄어쓰기
        if issue_count == 0:
            print("모든 항목이 기준에 적합합니다.")
        else:
            print(f"기준을 벗어난 항목이 {issue_count}개 있습니다.")

# JSON 파일 불러오기
with open("jamsil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 분석 실행
분석기 = WaterQualityAnalyzer(data)
results, issue_count = 분석기.analyze()
분석기.report(results, issue_count)
