c     ****************************************************************          
c     *                                                              *          
c     *                      f-90 module file_info                   *          
c     *                                                              *          
c     *                       written by : rhd                       *          
c     *                                                              *          
c     *                    last modified : 10/28/2025                *          
c     *                                                              *          
c     *     define the variables to support Fortran file numbers     *          
c     *     mainly for the input system (scan)                       *          
c     *                                                              *          
c     ****************************************************************          
c                                                                               
c                                                                               
      module file_info                                                          
      integer ::  inlun(10), outlun(2), filcnt              
      integer, parameter :: max_opened_input_files  = 10
      logical :: outing                                                            
      end module                                                                
                                                                                
