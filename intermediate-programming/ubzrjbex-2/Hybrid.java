/*
Brian Prost
Hybrid.java
19 October 2020
 */

package ubzrjbexGjb;

public class Hybrid extends Automobile {

//    miles per gallon field
    int mpg;

    public Hybrid(String makeAndModel, double purchasePrice, int mpg) {
        super(makeAndModel, purchasePrice);
        this.mpg = mpg;
    }

    @Override
    public double salesTax(double purchasePrice) {
        double salesTax = super.salesTax(purchasePrice);
        salesTax = salesTax - (100 + (2 * (mpg - 40)));

        return salesTax;
    }

    @Override
    public String toString() {
        String s = super.toString();
        s = s + '\n' +
                "Miles Per Gallon: " + mpg;
        return s;
    }
}
