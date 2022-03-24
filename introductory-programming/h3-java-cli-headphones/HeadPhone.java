/*
HeadPhone.java
Brian Prost
30 June 2020
this represents a headphone set
 */

import java.awt.Color;

public class HeadPhone {
    // constants
    public static final int LOW = 1;
    public static final int MEDIUM = 2;
    public static final int HIGH = 3;
    // other variables
    private int volume;
    private Boolean pluggedIn;
    private String manufacturer;
    private String headPhoneColor;
    private String headPhoneModel;

    // getters
    public int getVolume() {
        return volume;
    }

    public Boolean getPluggedIn() {
        return pluggedIn;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public String getHeadPhoneColor() {
        return headPhoneColor;
    }

    public String getHeadPhoneModel() {
        return headPhoneModel;
    }

    // setters
    public void setVolume(int volume) {
        this.volume = volume;
    }

    public void setPluggedIn(Boolean pluggedIn) {
        this.pluggedIn = pluggedIn;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public void setHeadPhoneColor(String headPhoneColor) {
        this.headPhoneColor = headPhoneColor;
    }

    public void setHeadPhoneModel(String headPhoneModel) {
        this.headPhoneModel = headPhoneModel;
    }

    public HeadPhone(int volume, Boolean pluggedIn, String manufacturer, String headPhoneColor, String headPhoneModel) {
        this.volume = volume;
        this.pluggedIn = pluggedIn;
        this.manufacturer = manufacturer;
        this.headPhoneColor = headPhoneColor;
        this.headPhoneModel = headPhoneModel;
    }

    public HeadPhone() {
        volume = MEDIUM;
        pluggedIn = false;
    }

    public void changeVolume(int v) {
        this.volume = v;
    }

    public String toString() {
        String theString = ("You are listening to music on the " + headPhoneColor + " " + headPhoneModel
                + " headphones manufactured by " + manufacturer + ".\nCurrently, the headphones are ");

        if (pluggedIn == true) {
            theString = theString + ("plugged in. ");

        } else {
            theString = theString + ("not plugged in. ");
        }
        theString = theString + ("The volume is set to " + volume + ". ");
        return theString;
    }

    public String toStringWithVolulmeChange() {
        String printWithVolume = ("The volume is now set to " + volume + ". ");
        if (volume == 3) {
            printWithVolume = printWithVolume + ("\n\nTURN IT DOWN!!!\n");
        } else if (volume > 3) {
            printWithVolume = printWithVolume
                    + ("Uh oh. Oh no...." + "\n...\nYou turned it up too loud and they blew. You owe us.");
        }
        return printWithVolume;
    }
}
