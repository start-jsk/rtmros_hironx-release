Name:           ros-hydro-hironx-ros-bridge
Version:        1.0.33
Release:        0%{?dist}
Summary:        ROS hironx_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hironx_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       gnuplot
Requires:       ros-hydro-hrpsys-ros-bridge
Requires:       ros-hydro-moveit-commander
Requires:       ros-hydro-openni2-launch
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-rosbash
Requires:       ros-hydro-roslang
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rospy
Requires:       ros-hydro-tf
BuildRequires:  gnuplot
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-hrpsys-ros-bridge
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-rosbash
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-roslang
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-roslint
BuildRequires:  unzip

%description
ROS-OpenRTM interfacing package for the opensource version of Kawada's
Hiro/NEXTAGE dual-arm robot. NOTE: This package is multi-license -- pay
attention to file header in each file where license is declared. For Creative
Commons nc 4.0 applied, see here.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Jul 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.32-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.31-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.30-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.29-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.28-0
- Autogenerated by Bloom

* Tue Nov 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.27-0
- Autogenerated by Bloom

* Tue Oct 07 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.26-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.25-0
- Autogenerated by Bloom

* Tue Sep 16 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.24-0
- Autogenerated by Bloom

* Tue Sep 02 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.23-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.22-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.21-0
- Autogenerated by Bloom

* Thu Jul 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Tue Jul 29 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-1
- Autogenerated by Bloom

* Mon Jul 28 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

