from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      Stock_symbol = 'TATA'
      Total_shares = 200
      Share_price = 50
      Buying_commission = 10
      Selling_Price = 100
      Selling_commission = 15
      Captial_Tax_percent = 10
      Stock_symbol = result['Stock_symbol']
      print(type(int(Total_shares)))
      print(result['Stock_symbol'])
      Total_shares = int(result['Total_shares'])
      Share_price = int(result['Share_price'])
      Buying_commission = int(result['Buying_commission'])
      Selling_Price = int(result['Selling_Price'])
      Selling_commission = int(result['Selling_commission'])
      Captial_Tax_percent = int(result['Captial_Tax_percent'])
      # calculating final_price and initial_price
      final_price = (Total_shares * Selling_Price) - Selling_commission
      print(final_price)
      initial_price = (Total_shares * Share_price) + Buying_commission
      print(initial_price)
      
      # calculating total_profit
      total_profit = final_price - initial_price
      print(total_profit)
      
      # caluclating tax
      tax = (Captial_Tax_percent / 100) * total_profit
      print(tax)
      
      # calculate final net_total_profit and cost_price
      net_total_profit = total_profit - tax
      cost_price = (Selling_Price * Total_shares) - net_total_profit
      print(cost_price)
      
      # calculating Rate_of_Interest
      Rate_of_Interest = ( ( (net_total_profit - cost_price) / cost_price ) * 100 ) + 100
      print(Rate_of_Interest)
      
      # calculating break_even
      break_even = Share_price+( Buying_commission + Selling_commission  )/100
      print(break_even)
      dict = {'Stock_symbol': Stock_symbol,'final_price':final_price,'initial_price':initial_price,'total_profit':total_profit}
      
      return render_template("student.html",result = dict)

if __name__ == '__main__':
   app.run(debug = True)