package ysy.baidu;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import org.junit.Test;

public class baidu {
    public static void main(String[] args) {
        baidu ysy = new baidu();
        ysy.getLatitude();
    }

    @Test
    public void getLatitude() {
        String inputaddress = "南京 南京航空大学将军路校区";
        try {
            // 1、将地址转换成UTF_8
            String address = URLEncoder.encode(inputaddress, StandardCharsets.UTF_8);

            // 2、请求位置信息
            URL resjson = new URL("http://api.map.baidu.com/geocoder?address="
                    + address + "&output=json&key=" + "mTp6zPE3VVQfYjbYiZO9gUf6aiDwcbvx");

            // 3、获取地址的内容
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    resjson.openStream()));
            String res;
            StringBuilder sb = new StringBuilder("");
            while(true){
                res = in.readLine();
                if(res == null) break;
                sb.append(res.trim());
            }
            in.close();
            String str = sb.toString();

            // 4、处理地址str
            if(!str.isEmpty()){
                int lngStart = str.indexOf("lng\":");
                int lngEnd = str.indexOf(",\"lat");
                int latEnd = str.indexOf("},\"precise");
                if (lngStart > 0 && lngEnd > 0 && latEnd > 0) {
                    String lng = str.substring(lngStart + 5, lngEnd);
                    String lat = str.substring(lngEnd + 7, latEnd);
                    System.out.println("地址：" + inputaddress + '\n'  + "经度：" + lng + '\n' + "纬度：" + lat);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
