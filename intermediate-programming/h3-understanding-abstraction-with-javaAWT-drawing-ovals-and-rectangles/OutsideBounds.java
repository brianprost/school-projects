/*
Brian Prost
OutsideBounds.java
custom exception
08 November 2020
 */

package homeworkGuerr;

import javax.swing.JOptionPane;

public class OutsideBounds extends Exception {

    OutsideBounds() {
        JOptionPane.showMessageDialog(null, "Your numbers were too big.",
                "This Isn't Supersize Me", JOptionPane.ERROR_MESSAGE);
        printStackTrace();
    }
}
