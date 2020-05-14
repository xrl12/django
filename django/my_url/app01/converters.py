class PhoneConverter:
    regex = '\d+'

    def to_python(self, value):
        print('这个是路由里面的',value)
        return int(value)

    def to_url(self, value):
        print('这个是路由里面的', value)
        return str(value)
    