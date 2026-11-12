package org.example;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;

public class Main {

    public static void main(String[] args) throws IOException {

        int c;

        Socket s = new Socket("whois.internic.net", 43);
        InputStream in = s.getInputStream();
        OutputStream out = s.getOutputStream();

        String str = (args.length == 0 ? "MHProfessional.com" : args[0]) + "\n";
        byte[] buf = str.getBytes();

        out.write(buf);

        String xs = "";
        while ((c = in.read()) != -1) {
            xs += (char) c;
        }


        System.out.println(xs);

        s.close();

        System.out.println(InetAddress.getLocalHost());

    }

}