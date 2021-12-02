/*
Brian Prost
Project2.java
19 October 2020
 */

package ubzrjbexGjb;

import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.text.NumberFormatter;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.NumberFormat;

public class Project2 extends JFrame {

//    create text fields and labels

//    make and model
    private JLabel makeAndModelLabel = new JLabel("Make and Model:");
    private JTextField makeAndModelField = new JTextField(15);

//    purchase price
    private JLabel purchasePriceLabel = new JLabel("Sales Price:");
    private JTextField purchasePriceField = new JTextField(15);

    private NumberFormat format = NumberFormat.getInstance();
    private NumberFormatter numberFormatter = new NumberFormatter(format);

//    mpg
    private JLabel mpgLabel = new JLabel("Miles per Gallon");
    private JFormattedTextField mpgField = new JFormattedTextField(numberFormatter);

//    weight
    private JLabel weightLabel = new JLabel("Weight in Pounds");
    private JFormattedTextField weightField = new JFormattedTextField(numberFormatter);

//    button group
    private ButtonGroup buttonGroup;

    //        radio buttons
    private JRadioButton hybridCar = new JRadioButton("Hybrid");
    private JRadioButton electricCar = new JRadioButton("Electric");
    private JRadioButton otherCar = new JRadioButton("Other");


//    buttons
    private JButton computeSalesTaxButton = new JButton("Compute Sales Tax");
    private JButton clearFieldsButton = new JButton("Clear Fields");
    private JButton displayReportButton = new JButton("Display Report");
    private JTextArea salesTaxDisplay = new JTextArea();

//    text area for results
    private JTextArea salesTotalArea = new JTextArea();

    private int count = 0;

    Automobile[] allCarData = new Automobile[5];


    public Project2() {
        super("Automobile Sales Tax Calculator");

        setSize(500,309);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

//        entry panel
        JPanel entryPanel = new JPanel();

        entryPanel.setLayout(new GridLayout(2,1,10,2));

//        make and model
        entryPanel.add(makeAndModelLabel);
        entryPanel.add(makeAndModelField);

//        purchase price
        entryPanel.add(purchasePriceLabel);
        entryPanel.add(purchasePriceField);

        add(entryPanel);

//        automobile type panel
        JPanel automobileTypePanel = new JPanel();
        automobileTypePanel.setLayout(new GridLayout(3,2,10,10));

//        make border
        TitledBorder automobileTypeLabelBorder;
        automobileTypeLabelBorder = BorderFactory.createTitledBorder("Automobile Type");
        automobileTypePanel.setBorder(automobileTypeLabelBorder);

        numberFormatter.setValueClass(Integer.class);
        numberFormatter.setMinimum(0);
        numberFormatter.setMaximum(Integer.MAX_VALUE);
        numberFormatter.setAllowsInvalid(false);
        numberFormatter.setCommitsOnValidEdit(true);
        format.setGroupingUsed(false);

        hybridCar.setActionCommand("hybrid");
        electricCar.setActionCommand("electric");
        otherCar.setActionCommand("other");

//        button group
        buttonGroup = new ButtonGroup();
        buttonGroup.add(hybridCar);
        buttonGroup.add(electricCar);
        buttonGroup.add(otherCar);

//        i literally can't get these to resize
        mpgField.setPreferredSize(new Dimension(100,25));
        weightField.setPreferredSize(new Dimension(100,25));

//        radio panel
        JPanel radioPanel = new JPanel(new GridLayout(0,1));
        radioPanel.add(hybridCar);
        radioPanel.add(electricCar);
        radioPanel.add(otherCar);
        add(radioPanel);

//        add to panel
        add(mpgLabel);
        add(mpgField);
        add(weightLabel);
        add(weightField);

        add(automobileTypePanel);

//        button panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(2,2,10,10));
        buttonPanel.add(computeSalesTaxButton);
        buttonPanel.add(clearFieldsButton);
        buttonPanel.add(displayReportButton);
        buttonPanel.add(salesTaxDisplay);
        add(buttonPanel);

//        action listener time
        automobileTypeSelection ats = new automobileTypeSelection();
        computeSalesTaxButton.addActionListener(ats);
        clearButton cb = new clearButton();
        clearFieldsButton.addActionListener(cb);
        displayReport dr = new displayReport();
        displayReportButton.addActionListener(dr);

    }

    private class automobileTypeSelection implements ActionListener  {
        @Override
        public void actionPerformed (ActionEvent e) {
            try {
                if (hybridCar.isSelected()) {
                    allCarData[count] = new Hybrid(makeAndModelField.getText(),
                            Double.parseDouble(purchasePriceField.getText()),
                            Integer.parseInt(mpgField.getText()));
                } else if (electricCar.isSelected()) {
                    allCarData[count] = new Electric(makeAndModelField.getText(),
                            Double.parseDouble(purchasePriceField.getText()),
                            Integer.parseInt(weightField.getText()));
                } else {
                    allCarData[count] = new Automobile(makeAndModelField.getText(),
                            Double.parseDouble(purchasePriceField.getText()));
                }
                salesTaxDisplay.setText("Sales Tax is $" + String.valueOf(allCarData[count].salesTax(Double
                        .parseDouble(purchasePriceField.getText()))));
                count++;
            } catch (ArrayIndexOutOfBoundsException outOfBoundsException) {
                System.out.println("Sorry, the array can only hold 5 cars. You don't need more than 5 cars, anyways.");
            } catch (NumberFormatException numberFormatException) {
                JOptionPane.showMessageDialog(null,"Please enter a valid Integer.");
            } catch (Exception exception) {
                System.out.println(exception);
            }

        }
    }

    private class clearButton implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            makeAndModelField.setText("");
            purchasePriceField.setText("");
            mpgField.setText("");
            weightField.setText("");
            salesTaxDisplay.setText("");
            buttonGroup.clearSelection();
        }
    }

    private class displayReport implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            for (Automobile allCarDatum : allCarData) {
                System.out.println(allCarDatum + "\n");
            }
        }
    }

    public static void main (String[] args) {
        new Project2().setVisible(true);
    }

}
