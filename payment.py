from onlinepayment import OnlinePayment

# connect to authorize.net, setup auth with login and key
auth= { 'login': 'YOUR LOGIN HERE',
        'key':   'YOUR KEY HERE' }

op = OnlinePayment('authnet', test_mode=True, auth=auth)

# or for paypal, setup auth with user, pass, vendor and product:
auth= { 'username': 'YOUR USERNAME HERE',
        'password': 'YOUR PASSWORD HERE',
        'vendor':   'YOUR VENDOR HERE',
        'product':  'YOUR PRODUCT HERE' }

# connect to PayPal
op = OnlinePayment('paypal', test_mode=True, auth=auth)

# charge a card
try:
    result = op.sale(first_name = 'Joe',
                     last_name  = 'Example',
                     address    = '100 Example Ln.',
                     city       = 'Exampleville',
                     state      = 'NY',
                     zip        = '10001',
                     amount     = '2.00',
                     card_num   = '4007000000027',
                     exp_date   = '0530',
                     card_code  = '1234')

except conn.TransactionDeclined:
   # do something when the transaction fails

except conn.CardExpired:
   # tell the user their card is expired

except conn.ProcessorException:
   # handle all other possible processor-generated exceptions generically

# examine result, the values returned here are processor-specific
success  = result.success
code     = result.code
message  = result.message
trans_id = result.trans_id

# you can get the raw data returned by the underlying processor too
orig = result.orig
