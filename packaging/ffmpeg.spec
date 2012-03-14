Name:       ffmpeg
Summary:    AV codec lib
Version:    0.8.5
Release:    2.37
Group:      TO_BE/FILLED_IN
License:    GPLv2
Source0:    ffmpeg-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
AV codec library


%package -n libswscale-devel
Summary:    AV codec lib (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n libswscale-devel
AV codec library (devel)

%package -n libavcodec-devel
Summary:    AV codec lib (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n libavcodec-devel
AV codec library (devel)

%package -n libavdevice-devel
Summary:    AV device lib (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n libavdevice-devel
AV device library (devel)

%package -n libavformat-devel
Summary:    AV format lib (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n libavformat-devel
AV format library (devel)

%package -n libavutil-devel
Summary:    AV util lib (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n libavutil-devel
AV util library (devel)


%prep
%setup -q 

export CONFIGURE_OPTIONS=" --disable-static    --enable-shared   --disable-postproc \
	--disable-version3  --disable-devices   --disable-nonfree --disable-gpl --disable-doc \
	--disable-mmx       --disable-zlib    --disable-network \
	--disable-ffserver  --disable-ffplay  --disable-ffmpeg  \
	--disable-avfilter  --enable-avdevice \
        --disable-bsfs      --disable-filters \
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
	--enable-demuxer=dv \
	--disable-decoders \
	--enable-decoder=alac   --enable-decoder=h264           --enable-decoder=wmv1 \
	--enable-decoder=flac   --enable-decoder=mpeg4          --enable-decoder=wmv2 \
	--enable-decoder=h263   --enable-decoder=mpegvideo      --enable-decoder=wmv3 \
	--enable-decoder=vc1 \
	--enable-decoder=h263i  --enable-decoder=theora	 \
        --enable-encoder=h263   --enable-encoder=h263p  --enable-encoder=mpeg4   \
        --enable-decoder=bmp  --enable-encoder=bmp       \
        --enable-decoder=tiff \
        --enable-decoder=mp3  --enable-decoder=amrnb    \
        --enable-encoder=aac  --enable-decoder=aac      \
	--enable-swscale	--disable-yasm "
CFLAGS="%{optflags} -fPIC -DEXPORT_API=\"__attribute__((visibility(\\\"default\\\")))\" "; export CFLAGS
./configure --prefix=%_prefix $CONFIGURE_OPTIONS

%build


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/*.so.*
/usr/bin/ffprobe
/usr/share/ffmpeg/*

%files -n libswscale-devel
/usr/include/libswscale/swscale.h
/usr/lib/libswscale.so
/usr/lib/pkgconfig/libswscale.pc

%files -n libavcodec-devel
%_includedir/libavcodec/*
%_libdir/libavcodec.so
%_libdir/pkgconfig/libavcodec.pc

%files -n libavdevice-devel
%_includedir/libavdevice/*
%_libdir/libavdevice.so
%_libdir/pkgconfig/libavdevice.pc

%files -n libavformat-devel
%_includedir/libavformat/*
%_libdir/libavformat.so
%_libdir/pkgconfig/libavformat.pc

%files -n libavutil-devel
%_includedir/libavutil/*
%_libdir/libavutil.so
%_libdir/pkgconfig/libavutil.pc

