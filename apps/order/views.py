# Django rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models imports
from .models import Order, OrderItem


class ListOrdersView(APIView):
    """
    API view to list orders for the authenticated user.
    """

    def get(self, request, format=None):
        """
        Handles the GET request to retrieve orders for the authenticated user.
        """
        # Get the authenticated user
        user = self.request.user

        try:
            # Query orders for the authenticated user, ordered by date in descending order
            orders = Order.objects.order_by('-date_issued').filter(user=user)
            result = []

            for order in orders:
                # Construct a dictionary with order information
                item = {}
                item['status'] = order.status
                item['transaction_id'] = order.transaction_id
                item['amount'] = order.amount
                item['shipping_price'] = order.shipping_price
                item['date_issued'] = order.date_issued
                item['address_line_1'] = order.address_line_1
                item['address_line_2'] = order.address_line_2

                result.append(item)

            # Return the list of order dictionaries in the response
            return Response(
                {'orders': result},
                status=status.HTTP_200_OK
            )
        except:
            # Handle any exceptions that might occur during order retrieval
            return Response(
                {'error': 'Something went wrong when retrieving orders'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListOrderDetailView(APIView):
    """
    API view to retrieve detailed information about a specific order.
    """

    def get(self, request, transactionId, format=None):
        """
        Handles the GET request to retrieve detailed information about a specific order.
        """

        # Get the authenticated user
        user = self.request.user

        try:
            # Check if an order with the provided transaction ID exists for the user
            if Order.objects.filter(user=user, transaction_id=transactionId).exists():
                order = Order.objects.get(user=user, transaction_id=transactionId)
                result = {}

                # Populate the result dictionary with order information
                result['status'] = order.status
                result['transaction_id'] = order.transaction_id
                result['amount'] = order.amount
                result['full_name'] = order.full_name
                result['address_line_1'] = order.address_line_1
                result['address_line_2'] = order.address_line_2
                result['city'] = order.city
                result['state_province_region'] = order.state_province_region
                result['postal_zip_code'] = order.postal_zip_code
                result['telephone_number'] = order.telephone_number
                result['shipping_name'] = order.shipping_name
                result['shipping_time'] = order.shipping_time
                result['shipping_price'] = order.shipping_price
                result['date_issued'] = order.date_issued

                # Query order items associated with the order
                order_items = OrderItem.objects.order_by('-date_added').filter(order=order)
                result['order_items'] = []

                # Populate the result dictionary with order item information
                for order_item in order_items:
                    sub_item = {}
                    sub_item['name'] = order_item.name
                    sub_item['price'] = order_item.price
                    sub_item['count'] = order_item.count
                    result['order_items'].append(sub_item)

                # Return the detailed order information in the response
                return Response(
                    {'order': result},
                    status=status.HTTP_200_OK
                )
            else:
                # Return an error response if the order does not exist
                return Response(
                    {'error': 'Order with this transaction ID does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            # Handle any exceptions that might occur during order detail retrieval
            return Response(
                {'error': 'Something went wrong when retrieving order detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )