Name:           ros-hydro-hironx-moveit-config
Version:        1.0.20
Release:        0%{?dist}
Summary:        ROS hironx_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/hironx_moveit_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-hironx-ros-bridge
Requires:       ros-hydro-moveit-planners
Requires:       ros-hydro-moveit-ros
Requires:       ros-hydro-pr2-moveit-plugins
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-collada-urdf
BuildRequires:  ros-hydro-hironx-ros-bridge
BuildRequires:  ros-hydro-moveit-ros-move-group

%description
An automatically generated package with all the configuration and launch files
for using the HiroNX with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Jul 31 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.20-0
- Autogenerated by Bloom

* Tue Jul 29 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-1
- Autogenerated by Bloom

* Mon Jul 28 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.19-0
- Autogenerated by Bloom

