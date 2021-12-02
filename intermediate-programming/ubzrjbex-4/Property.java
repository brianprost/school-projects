/*
 * Brian Prost
 * Property.java
 * Class implementing the StateChangeable interface. It constructs and instantiates a Property
 * 14 November 2020
 * */

package ubzrjbexSbhe;

public class Property<T extends Enum<T>> implements StateChangeable<T> {

    // instance variables
    String propertyAddress;
    int numOfBedrooms, squareFeet, price;
    Status propertyStatus;

    // constructor to initialize the characteristics of the property
    public Property(String propertyAddress, int numOfBedrooms, int squareFeet, int price) {
        this.propertyAddress = propertyAddress;
        this.numOfBedrooms = numOfBedrooms;
        this.squareFeet = squareFeet;
        this.price = price;
        this.propertyStatus = Status.FOR_SALE;
    }

    // changes the status of property
    @Override
    public void changeState(T newStatus) {
        this.propertyStatus = (Status) newStatus;
    }

    @Override
    public String toString() {
        return "\tProperty Details: " +
                "\nStreet Address: " + propertyAddress +
                "\nNumber of Bedrooms: " + numOfBedrooms +
                "\nSquare Feet: " + squareFeet +
                "\nPrice: $" + price +
                "\nProperty Status: " + propertyStatus;
    }
}
