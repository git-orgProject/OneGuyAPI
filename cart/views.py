from django.shortcuts import render

# Create your views here.

def cartshow(request):
    return render(request, 'cart/shopcart.html')


# from django.template.loader import get_template
# from django_redis import get_redis_connection
# from rest_framework.views import APIView
#
# from cart.models import CartModel
# from cart.serializers import CartSerializer
# from goods.models import CommodityModel
#
#
# class CartAPIView(APIView):
#     '''
#     因为我们APIView在我们调用http方法前会进行认证
#     我们的token过期或者伪造的化，会直接返回401
#     这个不符合业务逻辑
#     我们的业务逻辑应该是token过期或伪造的化应该认为是一个匿名用户
#     匿名用户的购物车数据可以放在cookie中
#     对于我们编程而言，应该能够先进入http方法，等验证用户信息是，再验证
#     '''
#
#     def perform_authentication(self, request):
#         pass
#
#     '''
#     当用户点击添加购物车按钮的时候
#     登陆用户需要将token sku_id count 选中状态提交给后端
#     未登陆用户需要将  sku_id  count 选中状态提交给后端
#
#     后端：1、接收数据（sku_id count selected）
#         2、验证数据 (验证商品的id是否有对应的商品，商品的个数）
#         3、获取数据
#         4、得到用户信息
#         5、根据用户的信息进行判断
#         6、登陆用户保存再redis中
#             6.1、链接redis
#             6.2、保存hash set
#             6.3返回响应
#         7、未登录用户 保存再cookie中
#             7.1 先读取cookie信息
#             7.2 判断是否有购物车信息
#                 如果有 加密处理
#                 如果没有
#             7.3 判断这个商品是否再cookie中
#                 如果在，累加数据
#                 如果不在则直接添加
#             7.4将购物车数据进行加密处理
#             7.5返回响应
#
#     '''
#
#     # 添加购物车
#     def post(self, request):
#
#         # 1、后端接收数据
#         data = request.data
#
#         # 2、验证数据(对应id是否有商品，商品的个数）
#         serializer = CartSerializer(data=data)
#
#         serializer.is_valid(raise_exception=True)
#
#         # 3、获取数据
#         sku_id = serializer.validated_data.get('sku_id')
#         count = serializer.validated_data.get('count')
#         selected = serializer.validated_data.get('selected')
#
#         # 4、得到用户的信息, 判断
#         try:
#             user = request.user
#         except Exception as e:
#             user = None
#
#         # 5、根据用户的信息进行判断
#         # request.user.is_authenticated
#         if user is not None and user.is_authenticated:
#             # user不为空，而且是认证用户
#             # 6、登陆用户保存在redis中
#             # 6.1链接redis
#             redis_conn = get_redis_connection('cart')
#             # 6.2保存数据
#             # hash
#             # 具体的存储方式需要查看文档才能确定
#             # redis_conn.hset('cart_%s'%user.id,sku_id,count)
#             # hash没有进行累加操作 应该累加
#             # hincrby 累加操作  累加数据可以是正数页可以是负数
#             # redis_conn.hincrby('cart_%s'%user.id,sku_id,count)
#             '''
#             管道
#             管道是基础redis类的子类，他为在单个请求中向服务器缓冲多个命令提供技术支持
#             他们可以用于通过减少客户端和服务器之间来回的tcp数据包数量来显著提高命令组的性能
#             A、创建管道
#             pl = redis_conn.pipeline()
#             B、将redis指令添加到管道中
#             pl.hincrby('cart_%s'%user.id,sku_id,count)
#
#             C、执行管道
#             pl.execute()
#
#             '''
#             pl = redis_conn.pipeline()
#
#             pl.hincrby('cart_%s' % user.id, sku_id, count)
#
#             # set
#             if selected:
#                 # redis_conn.sadd('cart_selected_%s'%user.id,sku_id)
#                 pl.sadd('cart_selected_%s' % user.id, sku_id)
#
#             pl.execute()
#             # 6.3返回数据
#             return Response(serializer.data)
#
#         else:
#             # 7、未登录用户保存在cookie中
#             # 7.1 先读取cookie信息
#             cookie_str = request.COOKIES.get('cart')
#             # 7.2判断是否有购物车信息
#             if cookie_str is not None:
#                 # 如果有，则是加密数据
#                 # 7.2.1  将加密后的数据进行解码
#                 decode = base64.b64decode(cookie_str)
#
#                 # 7.2.2 将二进制转化为字典
#                 cookie_cart = pickle.loads(decode)
#
#             else:
#                 # 如果没有，则定义一个空字典
#                 cookie_cart = {}
#
#             # 7.3判断这个商品是否在cookie中
#             if sku_id in cookie_cart:
#                 # 如果在 则累加，
#                 # 先获取之前的数据
#                 original_count = cookie_cart[sku_id]['count']
#
#                 count += original_count
#
#             # 如果不在，则直接添加
#             cookie_cart[sku_id] = {
#                 'count': count,
#                 'selected': selected
#             }
#
#             # 将购物车进行加密处理
#             # 7.4.1 将字典转化为bytes类型
#             dumps = pickle.dumps(cookie_cart)
#             # 7.4.2 对bytes类型进行编码
#             encode = base64.b64encode(dumps)
#
#             # 7.5返回响应
#             response = Response(serializer.data)
#
#             # 为啥要解码呢   将二进制转化为字符串
#             response.set_cookie('cart', encode.decode())
#
#             return response
#
#
# def perform_authentication(self, request):
#     pass
# class CartAPIView(object):
#     pass

# 1.先从cookie中，获取当前商品的购物车记录 (cart_json)
# 2.判断购物车(cart_json)数据是否存在，有可能用户从来没有操作过购物车
#     2.1.如果(cart_json)存在就把它转成字典(cart_dict)
#     2.2.如果(cart_json)不存在就定义空字典(cart_dict)
# 3.判断要添加的商品在购物车中是否存在
#     3.1.如果存在就取出源有值，并进行累加
#     3.2.如果不存在就直接保存商品数量
# 4.将(cart_dict)重新生成json字符串，方便写入到cookie
# 5.创建JsonResponse对象，该对象就是要响应的对象
# 6.在响应前，设置cookie信息
# 7.计算购物车数量总和，方便前端展示
