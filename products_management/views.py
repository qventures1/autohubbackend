"""
All view related to the products management

"""

from products_management.products_management_controller import ProductsManagement,CategoryMangement
from rest_framework.views import APIView


class ProductCategoryView(APIView):
    """CRUD Api view for the products Category"""
    category_controller=CategoryMangement()

    def post(self,request):

        return self.category_controller.add_category(request)

    def get(self,request):

        return self.category_controller.Show_Category(request)


    def patch(self,request):

        return self.category_controller.update_Category(request)

    def delete(self,request):

        return self.category_controller.delete_category(request)


class ProductsView(APIView):
    """CRUD Api view for the products"""

    products_controller = ProductsManagement()

    def post(self, request):
        """Create a product"""

        return self.products_controller.Add_product(request)



    def get(self,request):
        """get all products"""

        return self.products_controller.Show_products(request)

    def patch(self,request):
        """update all products"""

        return self.products_controller.update_product(request)

    def delete(self,request):
        """delete all products"""

        return self.products_controller.delete_product(request)


# class AddToCartView(APIView):
#     add_to_cart_controller=Add_To_Cart_Management()

#     def post(self,request):
#         """item add to cart"""

#         return self.add_to_cart_controller.add_to_cart(request)