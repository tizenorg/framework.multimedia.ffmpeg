Name:       ffmpeg
Summary:    AV codec lib
Version: 1.0.0
Release:    10
Group:      Multimedia
License:    LGPLv2.1
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
AV codec library


%package -n libavcodec
Summary:    AV codec lib
Group:      Multimedia

%description -n libavcodec
AV codec library

%package -n libavcodec-devel
Summary:    AV codec lib (devel)
Group:      Development/Libraries
Requires:   libavcodec = %{version}-%{release}

%description -n libavcodec-devel
AV codec library (devel)

%package -n libavformat
Summary:    AV format lib
Group:      Multimedia

%description -n libavformat
AV format library

%package -n libavformat-devel
Summary:    AV format lib (devel)
Group:      Development/Libraries
Requires:   libavformat = %{version}-%{release}

%description -n libavformat-devel
AV format library (devel)

%package -n libavutil
Summary:    AV util lib
Group:      Multimedia

%description -n libavutil
AV util library

%package -n libavutil-devel
Summary:    AV util lib (devel)
Group:      Development/Libraries
Requires:   libavutil = %{version}-%{release}

%description -n libavutil-devel
AV util library (devel)

%package -n libavfilter
Summary:    AV util lib
Group:      Multimedia

%description -n libavfilter
AV filter library

%package -n libavfilter-devel
Summary:    AV util lib (devel)
Group:      Development/Libraries
Requires:   libavfilter = %{version}-%{release}

%description -n libavfilter-devel
AV filter library (devel)

%package -n libswscale
Summary:    SW scale lib
Group:      Multimedia

%description -n libswscale
developement files for libswsacle

%package -n libswscale-devel
Summary:    SW scale lib (devel)
Group:      Development/Libraries
Requires:   libswscale = %{version}-%{release}

%description -n libswscale-devel
developement files for libswsacle


%prep
%setup -q

export CONFIGURE_OPTIONS="--enable-shared    --disable-static   --disable-postproc \
--disable-version3  --disable-devices   --disable-nonfree --disable-gpl --disable-doc \
--disable-zlib    --disable-network \
--disable-ffserver  --disable-ffplay  --disable-ffmpeg  --disable-ffprobe \
--disable-avdevice \
--disable-bsfs      --disable-filters \
--enable-filter=buffer  --enable-filter=buffersink      --enable-filter=crop \
--enable-filter=hflip   --enable-filter=lut     --enable-filter=lutyuv \
--enable-filter=lutrgb  --enable-filter=overlay --enable-filter=scale \
--enable-filter=transpose       --enable-filter=unsharp --enable-filter=vflip \
--disable-protocols \
--enable-protocol=file \
--disable-encoders \
--disable-muxers \
--disable-parsers \
--enable-parser=aac     --enable-parser=h264            --enable-parser=mpegaudio \
--enable-parser=h263    --enable-parser=mpeg4video      --enable-parser=mpegvideo \
--disable-demuxers \
--enable-demuxer=aac    --enable-demuxer=h264   --enable-demuxer=mpegts \
--enable-demuxer=amr    --enable-demuxer=m4v    --enable-demuxer=mpegtsraw \
--enable-demuxer=asf    --enable-demuxer=mmf    --enable-demuxer=mpegvideo \
--enable-demuxer=avi    --enable-demuxer=mov    --enable-demuxer=ogg \
--enable-demuxer=flac   --enable-demuxer=mp3    --enable-demuxer=wav \
--enable-demuxer=h263   --enable-demuxer=mpegps --enable-demuxer=matroska \
--enable-demuxer=dv	--enable-demuxer=flv \
--disable-decoders \
--enable-decoder=alac   --enable-decoder=h264           --enable-decoder=wmv1 \
--enable-decoder=flac   --enable-decoder=mpeg4          --enable-decoder=wmv2 \
--enable-decoder=h263   --enable-decoder=mpegvideo      --enable-decoder=wmv3 \
--enable-decoder=vc1	--enable-decoder=flv \
--enable-decoder=h263i  --enable-decoder=theora  \
--enable-decoder=pcm_alaw  --enable-decoder=pcm_mulaw  \
--enable-decoder=msmpeg4v3 \
--enable-encoder=h263   --enable-encoder=h263p  --enable-encoder=mpeg4   \
--enable-decoder=bmp  --enable-encoder=bmp       \
--enable-decoder=tiff \
--enable-decoder=mp3  --enable-decoder=amrnb    \
--enable-encoder=aac  --enable-decoder=aac      \
--enable-swscale        --disable-yasm	--disable-swresample	\
--enable-fft	--enable-rdft	--enable-mdct	--enable-neon --disable-stripping"

%ifarch %{arm}
export CONFIGURE_OPTIONS+=" --disable-mmx"
%else
%endif

CFLAGS="%{optflags} -fPIC -DEXPORT_API=\"__attribute__((visibility(\\\"default\\\")))\" "; export CFLAGS

%ifarch %{arm}
./configure --prefix=%{_prefix} $CONFIGURE_OPTIONS --extra-cflags="-mfpu=neon"
%else
./configure --prefix=%{_prefix} $CONFIGURE_OPTIONS
%endif

%build


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/%{_datadir}/license
cp -rf %{_builddir}/%{name}-%{version}/COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/libavcodec
cp -rf %{_builddir}/%{name}-%{version}/COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/libavformat
cp -rf %{_builddir}/%{name}-%{version}/COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/libavutil
cp -rf %{_builddir}/%{name}-%{version}/COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/libavfilter
cp -rf %{_builddir}/%{name}-%{version}/COPYING.LGPLv2.1 %{buildroot}/%{_datadir}/license/libswscale


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libavcodec
%manifest libavcodec.manifest
%defattr(-,root,root,-)
%{_libdir}/libavcodec.so.*
%{_datadir}/license/libavcodec

%files -n libavformat
%manifest libavformat.manifest
%defattr(-,root,root,-)
%{_libdir}/libavformat.so.*
%{_datadir}/license/libavformat

%files -n libavutil
%manifest libavutil.manifest
%defattr(-,root,root,-)
%{_libdir}/libavutil.so.*
%{_datadir}/license/libavutil

%files -n libavfilter
%manifest libavfilter.manifest
%defattr(-,root,root,-)
%{_libdir}/libavfilter.so.*
%{_datadir}/license/libavfilter

%files -n libswscale
%manifest libswscale.manifest
%defattr(-,root,root,-)
%{_libdir}/libswscale.so.*
%{_datadir}/license/libswscale

%files -n libavcodec-devel
%defattr(-,root,root,-)
%_includedir/libavcodec/*
%_libdir/libavcodec.so
%_libdir/pkgconfig/libavcodec.pc

%files -n libavformat-devel
%defattr(-,root,root,-)
%_includedir/libavformat/*
%_libdir/libavformat.so
%_libdir/pkgconfig/libavformat.pc

%files -n libavutil-devel
%defattr(-,root,root,-)
%_includedir/libavutil/*
%_libdir/libavutil.so
%_libdir/pkgconfig/libavutil.pc

%files -n libavfilter-devel
%defattr(-,root,root,-)
%_includedir/libavfilter/*
%_libdir/libavfilter.so
%_libdir/pkgconfig/libavfilter.pc

%files -n libswscale-devel
%defattr(-,root,root,-)
%_includedir/libswscale/*
%_libdir/libswscale.so
%_libdir/pkgconfig/libswscale.pc

