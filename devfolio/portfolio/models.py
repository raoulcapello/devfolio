from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Portfolio(models.Model):
    """Model describing Portfolio metadata."""

    # NOTE:
    # The three features image fields are configured as a FileField
    # instead of an ImageField, so they will also accept SVG, which is
    # not supported by Pillow (the third party library Django uses for
    # the ImageField).

    # NOTE:
    # Allowing SVG files can pose a security issue, since SVG files
    # can contain Javascript

    # Also see:
    # https://code.djangoproject.com/ticket/14092

    title = models.CharField(_("Title"), max_length=100)
    subtitle = models.CharField(_("Subtitle"), max_length=100, blank=True)
    description = models.TextField(
        _("Description"), max_length=300, blank=True
    )
    frontpage_greeting = models.CharField(
        _("Frontpage Greeting"), max_length=50, blank=True
    )
    featured_image = models.ImageField(
        _("Featured Image"),
        upload_to="images",
        blank=True,
    )
    resume = models.FileField(
        _("Resume"), upload_to="resume", max_length=100, blank=True
    )
    usp_main_image = models.ImageField(
        _("Unique Selling Points - Main Image"), upload_to="images", blank=True
    )
    usp1_title = models.CharField(
        _("Unique Selling Point 1 - Title"), max_length=30, blank=True
    )
    usp1_description = models.TextField(
        _("Unique Selling Point 1 - Description"), max_length=300, blank=True
    )
    usp1_image = models.FileField(
        _("Unique Selling Point 1 - Image"), upload_to="images", blank=True
    )
    usp2_title = models.CharField(
        _("Unique Selling Point 2 - Title"), max_length=30, blank=True
    )
    usp2_description = models.TextField(
        _("Unique Selling Point 2 - Description"), max_length=300, blank=True
    )
    usp2_image = models.FileField(
        _("Unique Selling Point 2 - Image"), upload_to="images", blank=True
    )
    usp3_title = models.CharField(
        _("Unique Selling Point 3 - Title"), max_length=30, blank=True
    )
    usp3_description = models.TextField(
        _("Unique Selling Point 3 - Description"), max_length=300, blank=True
    )
    usp3_image = models.FileField(
        _("Unique Selling Point 3 - Image"), upload_to="images", blank=True
    )

    class Meta:
        """Meta definition for Portfolio."""

        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def __str__(self):
        """Unicode representation of Portfolio."""
        return self.title

    def get_absolute_url(self):
        """Return absolute url for Portfolio."""
        return reverse("home")


class Project(models.Model):
    """Model definition for Project."""

    title = models.CharField(_("Title"), max_length=100)
    subtitle = models.CharField(_("Subtitle"), max_length=100, blank=True)
    description = models.TextField(
        _("Description"), max_length=300, blank=True
    )
    featured_image = models.ImageField(_("Featured Image"), upload_to="images")
    date = models.DateField(_("Date"), default=timezone.now)
    client = models.CharField(_("Client"), max_length=50, blank=True)
    services = models.CharField(_("Services"), max_length=100, blank=True)
    client_url = models.URLField(_("Client URL"), max_length=200, blank=True)
    live_url = models.URLField(_("Live URL"), max_length=200, blank=True)
    live_url_message_modal_title = models.CharField(
        _("Live URL Popup Title"), max_length=50, blank=True
    )
    live_url_message_modal_text = models.TextField(
        _("Live URL Popup Message"), max_length=300, blank=True
    )
    repo_url = models.URLField(_("Repo URL"), max_length=200, blank=True)
    objective_text = models.TextField(
        _("Objective"), max_length=500, blank=True
    )
    tools_n_tech_text = models.TextField(
        _("Tools and Tech"), max_length=500, blank=True
    )
    challenge_text = models.TextField(
        _("Challenge"), max_length=500, blank=True
    )
    share_fb = models.BooleanField(_("Share on FaceBook"), default=False)
    share_twitter = models.BooleanField(_("Share on Twitter"), default=False)

    class Meta:
        """Meta definition for Project."""

        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        """Unicode representation of Project."""
        return self.title

    def get_absolute_url(self):
        """Return absolute url for Project."""
        return reverse("portfolio:detail", kwargs={"id": self.id})


class Tag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(_("Title"), max_length=15)
    project = models.ManyToManyField("Project", verbose_name=_("Project"))

    class Meta:
        """Meta definition for Tag."""

        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        """Unicode representation of Tag."""
        return self.title


class Screenshot(models.Model):
    """
    Model definition for Screenshot.
    One or more can optionally be attached to a Portfolio Project.
    """

    caption = models.CharField(_("Caption"), max_length=50)
    screenshot = models.ImageField(_("Screenshot"), upload_to="screenshots")
    project = models.ForeignKey(
        "Project",
        verbose_name=_("Project"),
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for Screenshot."""

        verbose_name = "Screenshot"
        verbose_name_plural = "Screenshots"

    def __str__(self):
        """Unicode representation of Screenshot."""
        return f"{self.project}: {self.caption}"


class VideoURL(models.Model):
    """
    Model definition for VideoURL.
    One or more can optionally be attached to a Portfolio Project.
    """

    caption = models.CharField(_("Caption"), max_length=50)
    url = models.URLField(_("Video URL"), max_length=200)
    screenshot = models.ImageField(_("Screenshot"), upload_to="screenshots")
    project = models.ForeignKey(
        "Project",
        verbose_name=_("Project"),
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for VideoURL."""

        verbose_name = "VideoURL"
        verbose_name_plural = "VideoURLs"

    def __str__(self):
        """Unicode representation of VideoURL."""
        return f"{self.project}: {self.caption}"
