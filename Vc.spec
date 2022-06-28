#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : Vc
Version  : 1.4.3
Release  : 6
URL      : https://github.com/VcDevel/Vc/releases/download/1.4.3/Vc-1.4.3.tar.gz
Source0  : https://github.com/VcDevel/Vc/releases/download/1.4.3/Vc-1.4.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Vc-license = %{version}-%{release}
BuildRequires : Vc-dev
BuildRequires : buildreq-cmake

%description
###########################################
#################   AVX   #################
###########################################

%package dev
Summary: dev components for the Vc package.
Group: Development
Provides: Vc-devel = %{version}-%{release}
Requires: Vc = %{version}-%{release}

%description dev
dev components for the Vc package.


%package license
Summary: license components for the Vc package.
Group: Default

%description license
license components for the Vc package.


%package staticdev
Summary: staticdev components for the Vc package.
Group: Default
Requires: Vc-dev = %{version}-%{release}

%description staticdev
staticdev components for the Vc package.


%prep
%setup -q -n Vc-1.4.3
cd %{_builddir}/Vc-1.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656455492
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656455492
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vc
cp %{_builddir}/Vc-1.4.3/LICENSE %{buildroot}/usr/share/package-licenses/Vc/6c8c6d9c0fc3041e685edf9266d924ffd2e5002d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/Vc/Allocator
/usr/include/Vc/IO
/usr/include/Vc/Memory
/usr/include/Vc/SimdArray
/usr/include/Vc/Utils
/usr/include/Vc/Vc
/usr/include/Vc/algorithm
/usr/include/Vc/array
/usr/include/Vc/avx/casts.h
/usr/include/Vc/avx/const.h
/usr/include/Vc/avx/const_data.h
/usr/include/Vc/avx/debug.h
/usr/include/Vc/avx/deinterleave.tcc
/usr/include/Vc/avx/detail.h
/usr/include/Vc/avx/helperimpl.h
/usr/include/Vc/avx/intrinsics.h
/usr/include/Vc/avx/limits.h
/usr/include/Vc/avx/macros.h
/usr/include/Vc/avx/mask.h
/usr/include/Vc/avx/mask.tcc
/usr/include/Vc/avx/math.h
/usr/include/Vc/avx/shuffle.h
/usr/include/Vc/avx/simd_cast.h
/usr/include/Vc/avx/simd_cast_caller.tcc
/usr/include/Vc/avx/types.h
/usr/include/Vc/avx/vector.h
/usr/include/Vc/avx/vector.tcc
/usr/include/Vc/avx/vectorhelper.h
/usr/include/Vc/common/algorithms.h
/usr/include/Vc/common/aliasingentryhelper.h
/usr/include/Vc/common/alignedbase.h
/usr/include/Vc/common/bitscanintrinsics.h
/usr/include/Vc/common/const.h
/usr/include/Vc/common/data.h
/usr/include/Vc/common/deinterleave.h
/usr/include/Vc/common/detail.h
/usr/include/Vc/common/elementreference.h
/usr/include/Vc/common/exponential.h
/usr/include/Vc/common/fix_clang_emmintrin.h
/usr/include/Vc/common/gatherimplementation.h
/usr/include/Vc/common/gatherinterface.h
/usr/include/Vc/common/gatherinterface_deprecated.h
/usr/include/Vc/common/generalinterface.h
/usr/include/Vc/common/iif.h
/usr/include/Vc/common/indexsequence.h
/usr/include/Vc/common/interleave.h
/usr/include/Vc/common/interleavedmemory.h
/usr/include/Vc/common/iterators.h
/usr/include/Vc/common/loadinterface.h
/usr/include/Vc/common/loadstoreflags.h
/usr/include/Vc/common/logarithm.h
/usr/include/Vc/common/macros.h
/usr/include/Vc/common/makeContainer.h
/usr/include/Vc/common/make_unique.h
/usr/include/Vc/common/malloc.h
/usr/include/Vc/common/mask.h
/usr/include/Vc/common/maskbool.h
/usr/include/Vc/common/math.h
/usr/include/Vc/common/memory.h
/usr/include/Vc/common/memorybase.h
/usr/include/Vc/common/memoryfwd.h
/usr/include/Vc/common/operators.h
/usr/include/Vc/common/permutation.h
/usr/include/Vc/common/scatterimplementation.h
/usr/include/Vc/common/scatterinterface.h
/usr/include/Vc/common/scatterinterface_deprecated.h
/usr/include/Vc/common/set.h
/usr/include/Vc/common/simd_cast.h
/usr/include/Vc/common/simd_cast_caller.tcc
/usr/include/Vc/common/simdarray.h
/usr/include/Vc/common/simdarrayfwd.h
/usr/include/Vc/common/simdarrayhelper.h
/usr/include/Vc/common/simdize.h
/usr/include/Vc/common/simdmaskarray.h
/usr/include/Vc/common/span.h
/usr/include/Vc/common/storage.h
/usr/include/Vc/common/storeinterface.h
/usr/include/Vc/common/subscript.h
/usr/include/Vc/common/support.h
/usr/include/Vc/common/transpose.h
/usr/include/Vc/common/trigonometric.h
/usr/include/Vc/common/types.h
/usr/include/Vc/common/utility.h
/usr/include/Vc/common/vector.h
/usr/include/Vc/common/vector/casts.h
/usr/include/Vc/common/vectorabi.h
/usr/include/Vc/common/vectortraits.h
/usr/include/Vc/common/vectortuple.h
/usr/include/Vc/common/where.h
/usr/include/Vc/common/writemaskedvector.h
/usr/include/Vc/common/x86_prefetches.h
/usr/include/Vc/cpuid.h
/usr/include/Vc/fwddecl.h
/usr/include/Vc/global.h
/usr/include/Vc/iterators
/usr/include/Vc/limits
/usr/include/Vc/scalar/detail.h
/usr/include/Vc/scalar/helperimpl.h
/usr/include/Vc/scalar/limits.h
/usr/include/Vc/scalar/macros.h
/usr/include/Vc/scalar/mask.h
/usr/include/Vc/scalar/math.h
/usr/include/Vc/scalar/operators.h
/usr/include/Vc/scalar/simd_cast.h
/usr/include/Vc/scalar/simd_cast_caller.tcc
/usr/include/Vc/scalar/type_traits.h
/usr/include/Vc/scalar/types.h
/usr/include/Vc/scalar/vector.h
/usr/include/Vc/scalar/vector.tcc
/usr/include/Vc/simdize
/usr/include/Vc/span
/usr/include/Vc/sse/casts.h
/usr/include/Vc/sse/const.h
/usr/include/Vc/sse/const_data.h
/usr/include/Vc/sse/debug.h
/usr/include/Vc/sse/deinterleave.tcc
/usr/include/Vc/sse/detail.h
/usr/include/Vc/sse/helperimpl.h
/usr/include/Vc/sse/intrinsics.h
/usr/include/Vc/sse/limits.h
/usr/include/Vc/sse/macros.h
/usr/include/Vc/sse/mask.h
/usr/include/Vc/sse/mask.tcc
/usr/include/Vc/sse/math.h
/usr/include/Vc/sse/prefetches.tcc
/usr/include/Vc/sse/shuffle.h
/usr/include/Vc/sse/simd_cast.h
/usr/include/Vc/sse/simd_cast_caller.tcc
/usr/include/Vc/sse/type_traits.h
/usr/include/Vc/sse/types.h
/usr/include/Vc/sse/vector.h
/usr/include/Vc/sse/vector.tcc
/usr/include/Vc/sse/vectorhelper.h
/usr/include/Vc/sse/vectorhelper.tcc
/usr/include/Vc/support.h
/usr/include/Vc/traits/decay.h
/usr/include/Vc/traits/entry_type_of.h
/usr/include/Vc/traits/has_addition_operator.h
/usr/include/Vc/traits/has_contiguous_storage.h
/usr/include/Vc/traits/has_equality_operator.h
/usr/include/Vc/traits/has_multiply_operator.h
/usr/include/Vc/traits/has_no_allocated_data.h
/usr/include/Vc/traits/has_subscript_operator.h
/usr/include/Vc/traits/is_functor_argument_immutable.h
/usr/include/Vc/traits/is_implicit_cast_allowed.h
/usr/include/Vc/traits/is_index_sequence.h
/usr/include/Vc/traits/is_output_iterator.h
/usr/include/Vc/traits/type_traits.h
/usr/include/Vc/type_traits
/usr/include/Vc/vector
/usr/include/Vc/vector.h
/usr/include/Vc/version.h
/usr/lib64/cmake/Vc/AddCompilerFlag.cmake
/usr/lib64/cmake/Vc/CheckCCompilerFlag.cmake
/usr/lib64/cmake/Vc/CheckCXXCompilerFlag.cmake
/usr/lib64/cmake/Vc/FindVc.cmake
/usr/lib64/cmake/Vc/OptimizeForArchitecture.cmake
/usr/lib64/cmake/Vc/UserWarning.cmake
/usr/lib64/cmake/Vc/VcConfig.cmake
/usr/lib64/cmake/Vc/VcConfigVersion.cmake
/usr/lib64/cmake/Vc/VcMacros.cmake
/usr/lib64/cmake/Vc/VcTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Vc/VcTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vc/6c8c6d9c0fc3041e685edf9266d924ffd2e5002d

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libVc.a
