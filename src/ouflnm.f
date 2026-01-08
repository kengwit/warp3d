c     ****************************************************************
c     *                                                              *
c     *                      subroutine ouflnm                       *
c     *                                                              *
c     *                       written by : bh                        *
c     *                                                              *
c     *                   last modified : 1/6/26 rhd                 *
c     *                                                              *
c     *     creates a file name for patran output                    *
c     *     based on the output type and the step number.            *
c     *                                                              *
c     ****************************************************************
c
c
      subroutine ouflnm( strtnm, flnam, stepno )
      implicit none
c
      integer :: stepno
      character(len=4) :: strtnm
      character(len=*) :: flnam
c
      integer :: step_number  ! can be 7 digits
c
      step_number = stepno
      if( len(flnam) < 16 ) then
        write(*,9200)
        call die_gracefully
      end if
c
c                check to make sure the step number is not
c                greater than 7 digits.
c
      if( step_number .gt. 9999999 )
     &     step_number = step_number - 9999999
c
      flnam(1:) = ' '
      flnam(1:4) = strtnm  ! first part of name
      write(flnam(5:),9100) step_number
c
 9000 format(i4.4)
 9100 format(i7.7)
 9200 format('>>>> FATAL ERROR: invalid string length. ',
     &    'ouflnm.')
c
      end







