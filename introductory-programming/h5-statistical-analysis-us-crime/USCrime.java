/*
USCrime.java
Brian Prost
13 July 2020
This class will store the fields from the CSV file and also has the methods for
calculating data based on what the user wants
 */

// library imports
import java.util.ArrayList;
import java.util.List;

public class USCrime {

    // this will store the info from the CSV file
    static List<USCrime> crimeArrayList = new ArrayList<>();

    // declarations
    private int year;
    private int population;
    private int violentCrime;
    private double violentCrimeRate;
    private int murder;
    private double murderRate;
    private int rape;
    private double rapeRate;
    private int robbery;
    private double robberyRate;
    private int assault;
    private double assaultRate;
    private int poverty;
    private double povertyRate;
    private int burglary;
    private double burglaryRate;
    private int larceny;
    private double larcenyRate;
    private int vehicleTheft;
    private double vehicleTheftRate;

    // default constructor
    public USCrime(String[] args) {
        year = Integer.parseInt(args[0]);
        population = Integer.parseInt(args[1]);
        violentCrime = Integer.parseInt(args[2]);
        violentCrimeRate = Double.parseDouble(args[3]);
        murder = Integer.parseInt(args[4]);
        murderRate = Double.parseDouble(args[5]);
        rape = Integer.parseInt(args[6]);
        rapeRate = Double.parseDouble(args[7]);
        robbery = Integer.parseInt(args[8]);
        robberyRate = Double.parseDouble(args[9]);
        assault = Integer.parseInt(args[10]);
        assaultRate = Double.parseDouble(args[11]);
        poverty = Integer.parseInt(args[12]);
        povertyRate = Double.parseDouble(args[13]);
        burglary = Integer.parseInt(args[14]);
        burglaryRate = Double.parseDouble(args[15]);
        larceny = Integer.parseInt(args[16]);
        larcenyRate = Double.parseDouble(args[17]);
        vehicleTheft = Integer.parseInt(args[18]);
        vehicleTheftRate = Double.parseDouble(args[19]);
    }

    public int getYear() {
        return year;
    }

    public String getPopulation() {
        return String.format("%,d", population);
    }

    public int getViolentCrime() {
        return violentCrime;
    }

    public double getViolentCrimeRate() {
        return violentCrimeRate;
    }

    public int getMurder() {
        return murder;
    }

    public double getMurderRate() {
        return murderRate;
    }

    public int getRape() {
        return rape;
    }

    public double getRapeRate() {
        return rapeRate;
    }

    public int getRobbery() {
        return robbery;
    }

    public double getRobberyRate() {
        return robberyRate;
    }

    public int getAssault() {
        return assault;
    }

    public double getAssaultRate() {
        return assaultRate;
    }

    public int getPoverty() {
        return poverty;
    }

    public double getPovertyRate() {
        return povertyRate;
    }

    public int getBurglary() {
        return burglary;
    }

    public double getBurglaryRate() {
        return burglaryRate;
    }

    public int getLarceny() {
        return larceny;
    }

    public double getLarcenyRate() {
        return larcenyRate;
    }

    public int getVehicleTheft() {
        return vehicleTheft;
    }

    public double getVehicleTheftRate() {
        return vehicleTheftRate;
    }

    public List<USCrime> getCrimeArrayList() {
        return crimeArrayList;
    }

    public void setCrimeArrayList(List<USCrime> crimeArrayList) {
        USCrime.crimeArrayList = crimeArrayList;
    }

    static void buildList(String[] crimeStatItems) {
        USCrime crimeInstance = new USCrime(crimeStatItems);
        USCrime.crimeArrayList.add(crimeInstance);
    }

    static String getPercentagePopulationGrowth() {
        int currentPopulation, previousPopulation;
        double percentOfGrowth;
        StringBuilder sb = new StringBuilder("Years\t\t\tGrowth\n-------------------------------\n");
        for (int i = 1; i < crimeArrayList.size(); i++) {
            currentPopulation = crimeArrayList.get(i).population;
            previousPopulation = crimeArrayList.get(i - 1).population;
            sb.append(crimeArrayList.get(i - 1).year).append("-").append(crimeArrayList.get(i).year);
            percentOfGrowth = ((currentPopulation - previousPopulation) / (double) previousPopulation) * 100;
            sb.append("\t\t").append(String.format("%.4f", percentOfGrowth)).append("%\n");
        }
        return sb.toString();
    }

    public static int getHighestMurderRateYear() {
        int max = crimeArrayList.get(0).murder;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.murder > max) {
                max = aCrimeArrayList.murder;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }

    public static int getLowestMurderRateYear() {
        int min = crimeArrayList.get(0).murder;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.murder < min) {
                min = aCrimeArrayList.murder;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }

    public static int getHighestRobberyRateYear() {
        int max = crimeArrayList.get(0).robbery;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.robbery > max) {
                max = aCrimeArrayList.robbery;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }

    public static int getLowestRobberyRateYear() {
        int min = crimeArrayList.get(0).robbery;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.robbery < min) {
                min = aCrimeArrayList.robbery;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }

    public static int getHighestMotorVehicleTheftYear() {
        int max = crimeArrayList.get(0).vehicleTheft;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.vehicleTheft > max) {
                max = aCrimeArrayList.robbery;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }

    public static int getLowestMotorVehicleTheftYear() {
        int min = crimeArrayList.get(0).vehicleTheft;
        int year = crimeArrayList.get(0).year;
        for (USCrime aCrimeArrayList : crimeArrayList) {
            if (aCrimeArrayList.vehicleTheft < min) {
                min = aCrimeArrayList.robbery;
                year = aCrimeArrayList.year;
            }
        }
        return year;
    }
}
