c     ****************************************************************
c     *                                                              *
c     *                      subroutine ouocst                       *
c     *                                                              *
c     *                       written by : bh                        *
c     *                                                              *
c     *                   last modified : 1/7/26 rhd                 *
c     *                                                              *
c     *     opens or closes files for (1) patran binary or           *
c     *     formatted output, or (2) flat text or stream file        *
c     *     for nodal results                                        *
c     *                                                              *
c     ****************************************************************
c
      subroutine ouocst( stress, stepno, oubin, ouasc, bnfile,
     &                   fmfile, opt, out, flat_file,
     &                   stream_file, text_file, compressed,
     &                   flat_file_number )
      implicit none
c
      integer :: stepno, out, opt
      logical :: oubin, ouasc, stress, flat_file, stream_file, 
     &           text_file, compressed
c
c                       locals
c
      integer :: step_number, bnfile, fmfile, flat_file_number
      integer, external :: warp3d_get_device_number
      character(len=16) :: bflnam, fflnam
      character(len=4)  :: strtnm
      character(len=30) :: command
      character(len=30), save :: flat_name
      logical :: patran_file
!win      external system
c
c                       branch on whether files are to be opened
c                       (opt = 1) or closed (opt=2).
c
      step_number = stepno
      patran_file = oubin .or. ouasc
      if( step_number .gt. 9999999 )
     &     step_number = step_number - 9999999
c
      select case ( opt )
c
      case( 1 ) !  open files.
c
c                       attach patran binary file, if necessary.
c
c                       wn(be)(fe) or (fe)(fs) + step no  .MPI rank
c                            char*4              + i7.7
c
      if( patran_file .and. oubin ) then
         strtnm = 'wnbe'
         if( stress ) strtnm = 'wnbs'
         call ouflnm( strtnm, bflnam, step_number )
         bnfile = warp3d_get_device_number()
         open( unit=bnfile, file=bflnam, status='unknown',
     &         access='sequential', form='unformatted' )
      end if
c
c                       attach patran formatted file, if necessary.
c
      if( patran_file .and. ouasc ) then
         strtnm= 'wnfe'
         if( stress ) strtnm= 'wnfs'
         call ouflnm( strtnm, fflnam, step_number )
         fmfile = warp3d_get_device_number()
         open( unit=fmfile, file=fflnam, status='unknown',
     &         access='sequential', form='formatted' )
c
      end if
c
      if( patran_file ) return
c
c                       flat result file. name structure
c
c                        wne + step # + _text 
c                               i7.7          
c                        1-3   4-10      11-15   
c
c                        wns + step # + _stream 
c                        1-3    4-10     11-17  
c                               i7.7            
c
      flat_file_number = warp3d_get_device_number()
      flat_name(1:) = ' '
      flat_name(1:3)  = 'wne'
      if( stress ) flat_name(1:3)  = 'wns'
      write(flat_name(4:),9000) step_number
c
      if( stream_file ) then
        flat_name(11:) = '_stream'
        open( unit=flat_file_number, file=flat_name, status='unknown',
     &        access='stream', form='unformatted' )
        return
      end if
c
      if( text_file ) then
        flat_name(11:) = '_text'
        open( unit=flat_file_number, file=flat_name, status='unknown',
     &        access='sequential', form='formatted' )
        return
      end if
c
      return
c
c
      case ( 2 ) ! close files
c
c                       close patran file(s)
c
      if( patran_file ) then
         if( oubin ) close( bnfile, status='keep' )
         if( ouasc ) close( fmfile, status='keep' )
         return
      end if
c
c                       close flat file(s). compress text
c                       file if requested.
c
      if( flat_file ) then
         close(unit=flat_file_number,status='keep')
         if( .not. text_file ) return
         if( compressed ) then
           command(1:) = ' '
           command(1:) = 'gzip ' // flat_name
!win           result = system( command )
         end if
         return
      end if
c
      end select
c
 9000 format(i7.7)
 9100 format(i4.4)
c
      end

