# SPDX-License-Identifier: Apache-2.0
#!BuildTag: endpoint-copier-operator:v%%endpoint-copier-operator_version%%
#!BuildTag: endpoint-copier-operator:v%%endpoint-copier-operator_version%%-%RELEASE%
#!BuildTag: endpoint-copier-operator:latest
#!BuildVersion: 15.5
ARG SLE_VERSION
FROM registry.suse.com/bci/bci-micro:$SLE_VERSION AS micro

FROM registry.suse.com/bci/bci-base:$SLE_VERSION AS base
COPY --from=micro / /installroot/
RUN zypper --installroot /installroot --non-interactive install --no-recommends endpoint-copier-operator; zypper -n clean; rm -rf /var/log/*

FROM micro AS final
# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=com.suse.application.endpoint-copier-operator
LABEL org.opencontainers.image.authors="SUSE LLC (https://www.suse.com/)"
LABEL org.opencontainers.image.title="SLE endpoint-copier-operator Container Image"
LABEL org.opencontainers.image.description="endpoint-copier-operator based on the SLE Base Container Image."
LABEL org.opencontainers.image.version="%%endpoint-copier-operator_version%%"
LABEL org.opencontainers.image.url="https://www.suse.com/products/server/"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="SUSE LLC"
LABEL org.opensuse.reference="%%IMG_REPO%%/endpoint-copier-operator:v%%endpoint-copier-operator_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL com.suse.supportlevel="l3"
LABEL com.suse.eula="SUSE Combined EULA February 2024"
LABEL com.suse.lifecycle-url="https://www.suse.com/lifecycle"
LABEL com.suse.image-type="application"
LABEL com.suse.release-stage="released"
# endlabelprefix

#Install endpoint-copier-operator
COPY --from=base /installroot /
USER 65532:65532
ENTRYPOINT ["/usr/bin/manager"]
