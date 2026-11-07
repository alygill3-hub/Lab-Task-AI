# lab_screening.py

def check_eligibility(marks, papers_complete, conduct_clear, family_income):

    if not papers_complete:
        return "Hold", "Documents are incomplete"
    if marks < 70:
        return "Hold", "Marks are below the required minimum (70)"
    if not conduct_clear:
        return "Hold", "Conduct/disciplinary clearance not obtained"
    if family_income > 100000:
        return "Hold", "Family income is above the allowed limit (100,000)"

    return "Review", "Applicant satisfies all 4 conditions"


# Test cases
cases = [
    {
        "title": "Test 1: Everything OK",
        "data": (85, True, True, 60000),
        "expected": "Review",
        "note": "Good marks, complete papers, clear conduct, income within limit"
    },
    {
        "title": "Test 2: Conduct Not Clear",
        "data": (88, True, False, 50000),
        "expected": "Hold",
        "note": "High marks and complete papers, but conduct clearance is missing"
    },
    {
        "title": "Test 3: Income Too High",
        "data": (75, True, True, 140000),
        "expected": "Hold",
        "note": "Marks and conduct are fine, but family income is above 100k"
    },
    {
        "title": "Test 4: Boundary Values",
        "data": (70, True, True, 100000),
        "expected": "Review",
        "note": "Marks exactly 70 and income exactly 100,000"
    }
]


if __name__ == "__main__":
    print("=== Lab Task 2: Rule-Based Eligibility Check ===")
    total_passed = 0
    for case in cases:
        marks, papers, conduct, income = case["data"]
        result, reason = check_eligibility(marks, papers, conduct, income)
        status = "PASS" if result == case["expected"] else "FAIL"
        if status == "PASS":
            total_passed += 1

        print(case["title"])
        print(f"  Note     : {case['note']}")
        print(f"  Input    : Marks={marks}, Papers={papers}, Conduct={conduct}, Income={income}")
        print(f"  Expected : {case['expected']}")
        print(f"  Result   : {result}")
        print(f"  Reason   : {reason}")
        print(f"  Status   : {status}")
        print("-" * 60)

    print(f"Summary: {total_passed}/{len(cases)} tests passed")