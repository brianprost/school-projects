/*
Brian Prost
Electric.java
19 October 2020
 */

package homeworkGjb;

public class Electric extends Automobile {

//    weight in pounds because the US hates the metric system
    int weightInPounds;

    public Electric(String makeAndModel, double purchasePrice, int weightInPounds) {
        super(makeAndModel, purchasePrice);
        this.weightInPounds = weightInPounds;
    }

    @Override
    public double salesTax(double purchasePrice) {
        double salesTax = super.salesTax(purchasePrice);

        if (weightInPounds < 3000) {
            salesTax -= 200;
        } else {
            salesTax -= 150;
        }
        return salesTax;
    }

    @Override
    public String toString() {
        String s = super.toString();
        s = s + '\n' +
                "Weight: " + weightInPounds + " lbs.";
        return s;
    }
}
