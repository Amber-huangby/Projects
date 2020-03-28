import pytest

def test_1():
    a=1
    assert (a==1)

class Test_cl():
    def test0(self):
        b=0
        assert (b==0)

# def setup_module(login):
#     print("setup_module执行")






def test_2(login):
    a=2
    print("xiandayingbbbbb")

    assert (a==2)

def test_3(login):
    a=2
    print("xiandayingbbbbb")

    assert (a==2)


@pytest.fixture(params=['q',1,'ee'])
def test_4(request):
    return request.param

def test5(test_4):
    print("sdjfshd"+str(test_4))

if __name__ == '__main__':
    pytest.main()
