/**
Data:    2015-12-21
Status:  Tested on MSP430
input:   num need to sqrt
return:  result
Author:  xiaoxiami
*/
unsigned int sqrt_16(unsigned long M)
{
    uint16 result;
    uint16 i;
    unsigned long tmp, ttp;   
    if (M == 0)               
        return 0;
    
    result = 0;
    
    tmp = (M >> 30);          
    M <<= 2;
    if (tmp > 1)             
    {
        result ++;                 
        tmp -= result;
    }
    
    for (i=15; i>0; i--)     
    {
        result <<= 1;              
        
        tmp <<= 2;
        tmp += (M >> 30);     
        
        ttp = result;
        ttp = (ttp<<1)+1;
        
        M <<= 2;
        if (tmp >= ttp)       
        {
            tmp -= ttp;
            result ++;
        }
    }
    return result;
}