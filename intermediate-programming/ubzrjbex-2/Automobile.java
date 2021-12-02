/*
Brian Prost
Automobile.java
19 October 2020
 */

package ubzrjbexGjb;

public class Automobile {

//    make and model field
    String makeAndModel = "";

//    purchase price field
    double purchasePrice;

    public Automobile(String makeAndModel, double purchasePrice) {
        this.makeAndModel = makeAndModel;
        this.purchasePrice = purchasePrice;
    }

    //    salesTax method that returns base sales tax (5%)
    public double salesTax (double purchasePrice) {
        return purchasePrice * 0.05;
    }

    @Override
    public String toString() {
        return "Make and Model: " + makeAndModel + '\n' +
                "Sales Price: $" + purchasePrice + '\n' +
                "Sales Tax: $" + this.salesTax(this.purchasePrice);
    }
}
