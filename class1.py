class company:
    member1="krisha"
    member2="ravi"
    member3="sindu"
    member4="hema"
    def mem1(self):
        print("member1-working")
    def mem2(self):
        print("member2-not working")
s1=company()
print("member1 =",s1.member1)
print("member2 =",s1.member2)
print("member3 =",s1.member3)
print("member4 =",s1.member4)
s1.mem1()
s1.mem2()

