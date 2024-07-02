#!BuildTag: akri-webhook-configuration:latest
#!BuildTag: akri-webhook-configuration:v%PACKAGE_VERSION%
#!BuildTag: akri-webhook-configuration:v%PACKAGE_VERSION%-%RELEASE%
ARG SLE_VERSION
FROM registry.suse.com/bci/bci-micro:$SLE_VERSION AS micro

FROM registry.suse.com/bci/bci-base:$SLE_VERSION AS base
COPY --from=micro / /installroot/
RUN zypper --installroot /installroot --non-interactive install --no-recommends akri-webhook-configuration

FROM micro AS final

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=com.suse.application.akri
LABEL org.opencontainers.image.authors="SUSE LLC (https://www.suse.com/)"
LABEL org.opencontainers.image.title="SLE Akri Admission Controller Webhook Container Image"
LABEL org.opencontainers.image.description="akri-webhook-configuration based on the SLE Base Container Image."
LABEL org.opencontainers.image.version="%PACKAGE_VERSION%"
LABEL org.opencontainers.image.url="https://www.suse.com/solutions/edge-computing/"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="SUSE LLC"
LABEL org.opensuse.reference="%%IMG_REPO%%/akri-webhook-configuration:v%PACKAGE_VERSION%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL com.suse.supportlevel="techpreview"
LABEL com.suse.eula="SUSE Combined EULA February 2024"
LABEL com.suse.lifecycle-url="https://www.suse.com/lifecycle"
LABEL com.suse.image-type="application"
LABEL com.suse.release-stage="released"
# endlabelprefix

COPY --from=base /installroot /
ENV RUST_LOG agent,akri_debug_echo,akri_discovery_utils,akri_onvif,akri_opcua,akri_shared,akri_udev\ 
,controller,debug_echo_discovery_handler,onvif_discovery_handler,opcua_discovery_handler,udev_discovery_handler
ENTRYPOINT [ "/usr/bin/webhook-configuration" ]
