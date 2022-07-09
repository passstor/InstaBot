from instapy import InstaPy
import time
import test
start=time.time()
session=InstaPy(username='crypto_tyan',password='53V5p_cXb-%8fJEZ_5~z')
end=time.time()
print("1  ",end-start)#5
start=time.time()
session.login()
end=time.time()
print("2  ",end-start)#34
f = open('index.txt', 'r')
count=int(f.read())

while True:
    try:
        start=time.time()
        session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100,
                       skip_business=False,
                       skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[],
                       skip_bio_keyword=[],
                       mandatory_bio_keywords=[])
        end=time.time()
        print("3  ",end-start)#0
        start=time.time()
        session.set_user_interact(amount=1, randomize=True, percentage=100, media='Photo')
        end=time.time()
        print("4  ",end-start)#0
        start=time.time()
        session.set_do_like(enabled=True, percentage=70)
        end=time.time()
        print("5  ",end-start)#0
        start=time.time()
        session.interact_by_users("{}".format(test.l[count]), amount=1, randomize=True)
        end=time.time()
        print("6  ",end-start)#93
        f = open('index.txt', 'w')
        count+=1
        f.write(str(count))
        f.close
        print("number: ",count)
    except:
        pass
session.end()