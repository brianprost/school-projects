/*
HeadPhone.java
Brian Prost
30 June 2020
Tests HeadPhone Case
 */

//imports
import java.awt.Color;
import java.util.Scanner;

public class TestHeadPhone {
        public static void main(String[] args) {
                // declarations
                Scanner sc = new Scanner(System.in); // scanner
                HeadPhone headPhonesToListenTo = new HeadPhone(); // default headphone

                // Ask user which headphones they would like to try out.
                System.out.println(
                                "Select a pair of headphones to listen to.\n1. Overpriced Garbage\t2.Convenient Earbuds\t3.Audio Engineer's Headphones");
                int headPhoneChoice = sc.nextInt();

                // depending on user choice, set the headphone characteristics
                switch (headPhoneChoice) {
                        case 1:
                                headPhonesToListenTo = new HeadPhone(1, true, "Beats by Dre (now )", "red", "Solos");
                                break;
                        case 2:
                                headPhonesToListenTo = new HeadPhone(3, false, " Apple", "white", "AirPods");
                                break;
                        case 3:
                                headPhonesToListenTo = new HeadPhone(2, true, "Sennheiser", "navy-blue", "HD 600");
                                break;
                }

                // get calls
                int volume = headPhonesToListenTo.getVolume();
                Boolean pluggedIn = headPhonesToListenTo.getPluggedIn();
                String manufacturer = headPhonesToListenTo.getManufacturer();
                String color = headPhonesToListenTo.getHeadPhoneColor();
                String headPhoneModel = headPhonesToListenTo.getHeadPhoneModel();

                // print
                System.out.print(headPhonesToListenTo.toString());

                // ask if they would like to change the volume
                System.out.print("Would you like to change it?\t");
                char desireToChangeVolume = sc.next().charAt(0);

                // based on previous question, change volume or say goodbye
                switch (desireToChangeVolume) {
                        case 'y':
                                System.out.print("What would you like to change the volume to?\t");
                                int volumeChangeDesired = sc.nextInt();
                                headPhonesToListenTo.changeVolume(volumeChangeDesired);
                                System.out.println(headPhonesToListenTo.toStringWithVolulmeChange());
                                break;
                        default:
                                System.out.println("Okay then. Goodbye!");
                }
        }
}