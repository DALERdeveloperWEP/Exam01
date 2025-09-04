ball = int(input("ball: "))
if ball >= 90 and ball <= 100:
    print("A (A'lo)")
elif ball >= 80 and ball <= 89:
    print("B (Yaxshi)")
elif ball >= 70 and ball <= 79:
    print("C (Qoniqarli)")
elif ball >= 60 and ball <= 69:
    print("D (Qoniqarsiz)")
elif ball >= 0 and ball <= 59:
    print("F (Yomon)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")