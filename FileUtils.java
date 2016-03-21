package com.dilato.model.web.utils;

import java.awt.Image;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Iterator;

import javax.imageio.ImageIO;
import javax.imageio.ImageReadParam;
import javax.imageio.ImageReader;
import javax.imageio.stream.ImageInputStream;

public class FileUtils {

	
	public static void saveFile(File file, File dstfile, Long width, Long height) throws FileNotFoundException, IOException{
		
		//document.documentElement.clientWidth
		//document.documentElement.clientHeight
		FileInputStream is = null;  
        ImageInputStream iis = null;  
        
        is = new FileInputStream(file);
//		BufferedImage image = ImageIO.read(new FileInputStream(file)); 
		Iterator<ImageReader> it = ImageIO  
                .getImageReadersByFormatName("png");  
		ImageReader reader = it.next(); 
		ImageReadParam param = reader.getDefaultReadParam();  
		iis = ImageIO.createImageInputStream(is); 
		reader.setInput(iis, true); 
        
        
		Rectangle rect = new Rectangle(0, 0, width.intValue(), height.intValue());  
		
		param.setSourceRegion(rect);  
		 
		BufferedImage bi = reader.read(0, param);  
		
		if(dstfile.exists()){
			String absolutePath = dstfile.getAbsolutePath();
			dstfile.delete();
			ImageIO.write(bi, "png", new File(absolutePath)); 
		}
		else{
			ImageIO.write(bi, "png", dstfile);
		}
		
		
		
	}
}
