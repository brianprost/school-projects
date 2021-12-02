/*
* Weight.java
* Brian Prost
* 06 October 2020
* Project 1
*/
package ubzrjbexBar;

class Weight {

    // fields
    private int pounds;
    private double ounces;
    private static final int OUNCES_IN_A_POUND = 16;

    // default constructor
    public Weight(int pounds, double ounces) {
        this.pounds = pounds;
        this.ounces = ounces;
        this.toOunces();
        this.normalize();
    }

    public boolean lessThan(Weight w) {
        if (this.pounds < w.pounds) {
            return true;
        } else if (this.pounds > w.pounds) {
            return false;
        } else {
            if (this.ounces < w.ounces) {
                return true;
            } else {
                return false;
            }
        }
    }

    public void addTo(Weight w) {
        this.pounds += w.pounds;
        this.ounces += w.ounces;

    }

    public void divide(int x) {
        this.ounces = toOunces();
        this.ounces /= x;
        this.pounds = 0;

    }

    public String toString() {
        return this.pounds + " lbs\t" + this.ounces + " oz";
    }

    double toOunces() {
        return this.pounds * this.OUNCES_IN_A_POUND + this.ounces;
    }

    Weight normalize() {

        while (this.ounces > this.OUNCES_IN_A_POUND) {
            this.ounces -= this.OUNCES_IN_A_POUND;
            this.pounds++;
        }

        return this;
    }
}