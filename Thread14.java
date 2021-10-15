class SimpleThread implements Runnable
{  
  
   
  public void run()
    {  
     try
       {
         
         for(int i=1;i<=5;i++)
           {
          System.out.println(Thread.currentThread().getName()+" i value= "+i+"\n");
           Thread.sleep(500);
           }
       
        }
      catch(InterruptedException e)
        {
	  System.out.println(e);
        }    
    }  
}
 
class Thread14
  {
    public static void main(String args[])
     {  
 
      SimpleThread s=new SimpleThread();  
      Thread t1=new Thread(s,"One:");
      
      t1.start();  
      
      try
       {
        
          for(int i=1;i<=5;i++)
           {
             System.out.println("Main thread : i value="+i+"\n");
             Thread.sleep(1000);
            }
         
       }
       
       catch(InterruptedException e)
        {
	  System.out.println(e);
        }  
     }  
}  